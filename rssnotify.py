#!/usr/bin/env python
"""
rssnotify.py - Phenny RSSNotify Module
Copyright 2016, sfan5
Licensed under GNU General Public License v2.0
"""
import time
import re
import web
import os
import threading

import feedparser # sudo pip install feedparser

def to_unix_time(tstr):
	if tstr.endswith("Z"):
		tstr = tstr[:-1] + "+00:00"
	r = re.compile(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})([-+])(\d{2}):(\d{2})")
	g = r.match(tstr).groups(1)
	# This function would be like 100% shorter if the time library didn't suck so hard.
	# time.strptime completly ignores timezones because who needs timezones anyway?
	# time.timezone is only for non-DST; nobody reading 'time.timezone' in code expects that
	# you have time.gmtime() but you can't use it because time.mktime() fucks with it when it's DST
	# </rant>
	ts = time.mktime(time.strptime(g[0], "%Y-%m-%dT%H:%M:%S"))
	ts -= (time.altzone if time.daylight else time.timezone)
	if g[1] == "+":
		ts -= int(g[2]) * 60 * 60
		ts -= int(g[3]) * 60
	else: # g[1] == "-"
		ts += int(g[2]) * 60 * 60
		ts += int(g[3]) * 60
	return ts

def resolve_channels(phenny, l):
	ret = set()
	for entry in l:
		sign = 1
		if entry[0] == "-":
			entry = entry[1:]
			sign = -1
		c = phenny.bot.channels if entry == "*" else [entry]
		if sign == 1:
			ret |= set(c)
		else: # sign == -1
			ret -= set(c)
	return ret

class RssNotify():
	def __init__(self, config):
		self.config = config
		self.last_updated = {}
		self.last_check = 0
		self.firstrun = True
		for i in range(len(self.config["feeds"])):
			self.last_updated[i] = 0
	def needs_check(self):
		return time.time() > self.last_check + self.config["check_interval"]
	def check(self, phenny):
		start = self.last_check = time.time()
		print("[RssNotify]: Checking RSS feeds...")
		for fid, feedspec in enumerate(self.config["feeds"]):
			feed = feedparser.parse(feedspec[0], agent="Mozilla/5.0 (compatible; MinetestBot)")
			updated = 0
			for entry in feed.entries:
				if self.firstrun:
					break
				if self.last_updated[fid] >= to_unix_time(entry.updated):
					continue
				message = self._format_msg(entry)
				self._announce(phenny, message, feedspec[1])
				if self.config["logfile"] is not None:
					with open(self.config["logfile"], "a", encoding="utf-8") as f:
						message = self._format_msg(entry, log_format=True)
						f.write(message)
						f.write("\n")
				updated += 1
			new_time = max((to_unix_time(e.updated) for e in feed.entries), default=0)
			if new_time > self.last_updated[fid]:
				self.last_updated[fid] = new_time
			if updated > 0:
				print("[RssNotify]: Found %d update(s) for '%s'" % (updated, feedspec[0]))
		if self.firstrun:
			self.firstrun = False
		print("[RssNotify]: Checked %d RSS feeds in %0.3f seconds" % (len(self.config["feeds"]), time.time()-start))
	def _shorten(self, link):
		# We can utilitze git.io to shorten *.github.com links
		l, code = web.post("https://git.io/create", {'url': link})
		if code != 200:
			return None
		l = str(l, 'utf-8')
		if ' ' in l: # spaces means there was an error :(
			return None
		return "https://git.io/" + l
	def _format_msg(self, feed_entry, log_format=False):
		if log_format:
			f_cshort = "[color=#c00]%s[/color]"
			f_clong = "[color=#c00]%s[/color] ([color=#c00]%s[/color])"
			f_all = "[color=#3465a4][git][/color] %s -> [color=#73d216]%s[/color]: [b]%s[/b] [color=#a04265]%s[/color] %s ([color=#888a85]%s[/color])"
		else:
			f_cshort = "\x0304%s\x0f"
			f_clong = "\x0304%s\x0f (\x0304%s\x0f)"
			f_all = "\x0302[git]\x0f %s -> \x0303%s\x0f: \x02%s\x0f \x0313%s\x0f %s (\x0315%s\x0f)"
		committer_realname = feed_entry.authors[0].name
		if committer_realname == "":
				try:
					committer_realname = feed_entry.authors[0].email
				except AttributeError:
					committer_realname = ""
		try:
			committer = feed_entry.authors[0].href.replace('https://github.com/',"")
		except AttributeError:
			committer = committer_realname # This will only use the realname if the nickname couldn't be obtained
		m = re.search(r'/([a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+)/commit/([a-f0-9]{7})', feed_entry.links[0].href)
		repo_name = m.group(1) if m else "?"
		commit_hash = m.group(2) if m else "???????"
		commit_time = feed_entry.updated
		commit_text = feed_entry.title
		if self.config["show_link"]:
			commit_link = feed_entry.link
			if self.config["shorten_link"]:
				commit_link = self._shorten(commit_link) or commit_link
		else:
			commit_link = ""
		if committer_realname == "" or committer_realname.lower() == committer.lower():
			committer_final = f_cshort % committer
		else:
			committer_final = f_clong % (committer, committer_realname)
		return f_all % (committer_final, repo_name, commit_text, commit_hash, commit_link, commit_time)
	def _announce(self, phenny, message, chans):
		chans = resolve_channels(phenny, chans)
		for ch in chans:
			phenny.write(['PRIVMSG', ch], message)

#################

c = ['*', '-#minetest-hub']
rssn = RssNotify({
	"check_interval": 120,
	"show_link": True,
	"shorten_link": True,
	"logfile": os.getcwd() + "/rssnotify.log",
	"feeds": [
		('https://github.com/minetest/minetest/commits/master.atom', c),
		('https://github.com/minetest/minetest_game/commits/master.atom', c),
		('https://github.com/minetest/minetestmapper/commits/master.atom', c),
		('https://github.com/minetest/serverlist/commits/master.atom', c),
		('https://github.com/sfan5/phenny/commits/master.atom', ['##minetestbot']),
		('https://github.com/sfan5/minetestbot-modules/commits/master.atom', ['##minetestbot']),
	],
})

def rsscheck(phenny, input):
	if not rssn.needs_check():
		return
	t = threading.Thread(target=rssn.check, args=(phenny, ))
	t.start()

rsscheck.priority = 'low'
rsscheck.rule = r'.*'
rsscheck.event = '*'
rsscheck.thread = False
rsscheck.nohook = True

if __name__ == '__main__':
	print(__doc__.strip())
