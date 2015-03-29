#!/usr/bin/env python
"""
rssnotify.py - Phenny RssNotify Module
Copyright 2013, sfan5
Licensed under GNU General Public License v2.0
"""
import time
import re
import web
import os
import feedparser # sudo pip install feedparser
rssnotify = {}

def to_unix_time(tstr):
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

def excepta(arr, exclude):
	o = []
	for el in arr:
		if not el in exclude:
			o.append(el)
	return o

rssnotify["last_updated_feeds"] = {}
rssnotify["logfilepath"] = os.getcwd() + "/rssnotify.log"
rssnotify["dont_print_first_message"] = True # prevents spam when restarting the bot/reloading the module
rssnotify["update_cooldown"] = 60 # in seconds
rssnotify["show_commit_link"] = True
rssnotify["use_git.io"] = True
rssnotify["last_update"] = time.time() - rssnotify["update_cooldown"]

def rsscheck(phenny, input):
	t = time.time()
	if rssnotify["last_update"] > t-rssnotify["update_cooldown"]:
		return
	rssnotify["last_update"] = t
	print("[RssNotify]: Checking RSS Feeds...")
	start = time.time()
	allchans = excepta(phenny.bot.channels, ['##minebest'])
	feeds = [
		('https://github.com/minetest/minetest/commits/master.atom', allchans),
		('https://github.com/minetest/minetest_game/commits/master.atom', allchans),
		('https://github.com/minetest/minetestmapper/commits/master.atom', allchans),
		('https://github.com/minetest/master-server/commits/master.atom', allchans),
		('https://github.com/Uberi/MineTest-WorldEdit/commits/master.atom',  allchans),
		('https://github.com/Jeija/minetest-mod-mesecons/commits/master.atom', allchans),
		('https://github.com/sfan5/phenny/commits/master.atom', ['##minetestbot']),
		('https://github.com/sfan5/minetestbot-modules/commits/master.atom', ['##minetestbot']),
	]
	for v in range(0, len(feeds)):
		url = feeds[v][0]
		feednum = v
		options = {
			'agent': 'Mozilla/5.0 (MinetestBot)',
			'referrer': 'http://minetest.net'
		}
		feed = feedparser.parse(url, **options)
		updcnt = 0
		for feed_entry in feed.entries:
			if not feednum in rssnotify["last_updated_feeds"].keys():
				rssnotify["last_updated_feeds"][feednum] = -1
			if rssnotify["last_updated_feeds"][feednum] < to_unix_time(feed_entry.updated):
				commiter_realname = feed_entry.authors[0].name
				if commiter_realname == "":
						try:
							commiter_realname = feed_entry.authors[0].email
						except AttributeError:
							commiter_realname = "Unknown"
				try:
					commiter = feed_entry.authors[0].href.replace('https://github.com/',"")
				except AttributeError:
					commiter = commiter_realname # This will only use the realname if the nickname couldn't be obtained
				reponame = url.replace("https://github.com/","").replace("/commits/master.atom","")
				commit_hash = feed_entry.links[0].href.replace("https://github.com/" + reponame + "/commit/","")[:7]
				commit_time = feed_entry.updated
				updcnt += 1
				if rssnotify["dont_print_first_message"]:
					continue
				if rssnotify["show_commit_link"]:
					if rssnotify["use_git.io"]:
						# Side note: git.io only works with *.github.com links
						l, code = web.post("http://git.io/create", {'url': feed_entry.link})
						if code == 200:
							l = str(l, 'utf-8')
							if not ' ' in l: # If there are spaces it's probably an error
								commit_link = "http://git.io/" + l
							else:
								commit_link = feed_entry.link
						else:
							commit_link = feed_entry.link
					else:
						commit_link = feed_entry.link
				else:
					commit_link = ""

				chans = []
				if feeds[v][1] == '*':
					chans = phenny.bot.channels
				elif type(feeds[v][1]) == type([]):
					chans = feeds[v][1]
				else:
					print("[RssNotify]: Something went wrong!")
				if rssnotify["logfilepath"] != "":
					lf = open(rssnotify["logfilepath"], "a")
					if commiter.lower() != commiter_realname.lower():
						lf.write("[color=#3465a4][git][/color] [color=#cc0000]%s[/color] ([color=#cc0000]%s[/color]) -> [color=#73d216]%s[/color]: [b]%s[/b] [color=#a04265]%s[/color] %s ([color=#888a85]%s[/color])\n" % (commiter, commiter_realname, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
					else:
						lf.write("[color=#3465a4][git][/color] [color=#cc0000]%s[/color] -> [color=#73d216]%s[/color]: [b]%s[/b] [color=#a04265]%s[/color] %s ([color=#888a85]%s[/color])\n" % (commiter, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
					lf.close()
				for ch in chans:
					if commiter.lower() != commiter_realname.lower():
						phenny.write(['PRIVMSG', ch], "\x0302[git]\x0f \x0304%s\x0f (\x0304%s\x0f) -> \x0303%s\x0f: \x02%s\x0f \x0313%s\x0f %s (\x0315%s\x0f)" % (commiter, commiter_realname, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
					else:
						phenny.write(['PRIVMSG', ch], "\x0302[git]\x0f \x0304%s\x0f -> \x0303%s\x0f: \x02%s\x0f \x0313%s\x0f %s (\x0315%s\x0f)" % (commiter, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
		if len(feed.entries) > 0:
			m = -1
			for i in range(0, len(feed.entries)):
				if to_unix_time(feed.entries[i].updated) > m:
					m = to_unix_time(feed.entries[i].updated)
			rssnotify["last_updated_feeds"][feednum] = m
		if updcnt > 0:
			print("[RssNotify]: Found %i RSS Update(s) for URL '%s'" % (updcnt, url))
	end = time.time()
	if rssnotify["dont_print_first_message"]:
		rssnotify["dont_print_first_message"] = False
	print("[RssNotify]: Checked " + str(len(feeds)) + " RSS Feeds in %0.3f seconds" % (end-start))

rsscheck.priority = 'medium'
rsscheck.rule = r'.*'
rsscheck.event = '*'
rsscheck.nohook = True

if __name__ == '__main__':
	print(__doc__.strip())
