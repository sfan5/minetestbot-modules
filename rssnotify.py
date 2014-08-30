#!/usr/bin/env python
"""
rssnotify.py - Phenny RssNotify Module
Copyright 2013, sfan5
"""
import time
import re
import web
import feedparser # sudo pip install feedparser
rssnotify = {}

def to_unix_time(st): # not really accurate, but works
	reg = re.compile("([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})")
	g = reg.match(st).groups(1)
	t = 0
	t += int(g[5])
	t += int(g[4]) * 60
	t += int(g[3]) * 60 * 60
	t += int(g[2]) * 60 * 60 * 24
	t += int(g[1]) * 60 * 60 * 24 * 30
	t += int(g[0]) * 60 * 60 * 24 * 30 * 12
	return t

def excepta(arr, exclude):
	o = []
	for el in arr:
		if not el in exclude:
			o.append(el)
	return o

rssnotify["last_updated_feeds"] = {}

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
							if len(l.strip()) == 6:
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
				for ch in chans:
					if commiter.lower() != commiter_realname.lower():
						phenny.write(['PRIVMSG', ch], "\x0302[Git]\x0f \x0304%s\x0f (\x0304%s\x0f) -> \x0303%s\x0f: \x02%s\x0f \x0313%s\x0f %s (\x0315%s\x0f)" % (commiter, commiter_realname, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
					else:
						phenny.write(['PRIVMSG', ch], "\x0302[Git]\x0f \x0304%s\x0f -> \x0303%s\x0f: \x02%s\x0f \x0313%s\x0f %s (\x0315%s\x0f)" % (commiter, reponame, feed_entry.title, commit_hash, commit_link, commit_time))
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
