#!/usr/bin/env python
"""
rssnotify.py - Phenny RssNotify Module
Copyright 2013, Sfan5
"""
import feedparser, time, urllib, re # sudo easy_install feedparser
rssnotify = {}

def get_arrayindex(array,val):
    for i in range(0,len(array)):
        if array[i] == val:
            return i
    return -1

def to_unix_time(st): # not really accurate
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

rssnotify["last_updated_feeds"] = {}

rssnotify["dont_print_first_message"] = True
rssnotify["update_cooldown"] = 60 # in seconds
rssnotify["show_commit_link"] = True
rssnotify["use_git.io"] = True
rssnotify["last_update"] = time.time() - rssnotify["update_cooldown"]


def rsscheck(phenny, input):
    t = time.time()
    if rssnotify["last_update"] > t-rssnotify["update_cooldown"]:
        return
    rssnotify["last_update"] = t
    print("[LOG]: Checking RSS Feeds...")
    start = time.time()
    feeds = [
        'https://github.com/minetest/minetest/commits/master.atom', 
        'https://github.com/minetest/minetest_game/commits/master.atom',
        'https://github.com/minetest/common/commits/master.atom',
        'https://github.com/minetest/build/commits/master.atom',
        'https://github.com/minetest/survival/commits/master.atom',
        'https://github.com/Uberi/MineTest-WorldEdit/commits/master.atom', 
        'https://github.com/Jeija/minetest-mod-mesecons/commits/master.atom'
    ]
    for url in feeds:
        options = {
            'agent': 'Mozilla/5.0 (MinetestBot)',
            'referrer': 'http://minetest.net'
        }
        feed = feedparser.parse(url, **options)
        updcnt = 0
        for feed_entry in feed.entries:
            feednum = get_arrayindex(feeds, url)
            if not feednum in rssnotify["last_updated_feeds"].keys():
                rssnotify["last_updated_feeds"][feednum] = -1
            if rssnotify["last_updated_feeds"][feednum] < to_unix_time(feed_entry.updated):
                commiter_realname = feed_entry.authors[0].name
                try:
                    commiter = feed_entry.authors[0].href.replace('https://github.com/',"")
                except AttributeError:
                    commiter = commiter_realname # This will only print the Realname if the nickname couldn't be obtained
                if commiter_realname == "":
                        try:
                            commiter_realname = feed_entry.authors[0].email
                        except AttributeError:
                            commiter_realname = "Unknown"
                reponame = url.replace("https://github.com/","").replace("/commits/master.atom","")
                commit_hash = feed_entry.links[0].href.replace("https://github.com/" + reponame + "/commit/","")[:10]
                commit_time = feed_entry.updated
                updcnt += 1
                if rssnotify["dont_print_first_message"]:
                    continue # Don't print first Messages
                if rssnotify["show_commit_link"]:
                    if rssnotify["use_git.io"]:
                        params = urllib.urlencode({'url' : feed_entry.link}) # git.io only works with *.github.com links
                        u = urllib.urlopen("http://git.io/create", params)
                        commit_link = "http://git.io/" + u.read()
                    else:
                        commit_link = feed_entry.link
                else:               
                    commit_link = ""
                
                for ch in phenny.bot.channels:
                    if commiter.lower() != commiter_realname.lower():
                        #phenny.say("GIT: %s (%s) commited to %s: %s %s %s" % (commiter,commiter_realname,reponame,feed_entry.title,commit_hash,commit_time))
                        phenny.write(['PRIVMSG', ch],"GIT: %s (%s) commited to %s: %s %s %s %s" % (commiter, commiter_realname, reponame, feed_entry.title, commit_hash, commit_time, commit_link))
                    else:
                        #phenny.say("GIT: %s commited to %s: %s %s %s" % (commiter,reponame,feed_entry.title,commit_hash,commit_time))
                        phenny.write(['PRIVMSG', ch],"GIT: %s commited to %s: %s %s %s %s" % (commiter, reponame, feed_entry.title, commit_hash, commit_time, commit_link))
        if len(feed.entries) > 0:
            rssnotify["last_updated_feeds"][feednum] = to_unix_time(feed.entries[0].updated)
        if updcnt > 0:
            print("[LOG]: Found %i RSS Update(s) for URL '%s'" % (updcnt, url))
    end = time.time()
    if rssnotify["dont_print_first_message"]:
        rssnotify["dont_print_first_message"] = False
    print("[LOG]: Checked " + str(len(feeds)) + " RSS Feeds in %0.3f seconds" % (end-start))

rsscheck.priority = 'high'
rsscheck.rule = r'.*'
rsscheck.event = '*'
rsscheck.thread = True

if __name__ == '__main__': 
    print __doc__.strip()
