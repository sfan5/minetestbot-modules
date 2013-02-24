#!/usr/bin/env python
"""
rssnotify.py - Phenny RssNotify Module
Copyright 2012, Sfan5
"""
import feedparser, time, urllib # sudo easy_install feedparser
rssnotify = {}

def get_arrayindex(array,val):
    for i in range(0,len(array)):
        if array[i] == val:
            return i
    return -1

rssnotify["last_updated_feeds"] = {}

rssnotify["last_update"] = time.time()
rssnotify["dont_print_first_message"] = True
rssnotify["update_cooldown"] =60 # in seconds
rssnotify["show_commit_link"] = True
rssnotify["use_git.io"] = True



def rsscheck(phenny, input):
    t = time.time()
    if rssnotify["last_update"] > t-rssnotify["update_cooldown"]:
        return
    rssnotify["last_update"] = t
    print("[LOG]: Checking RSS Feeds...")
    start = time.time()
    feeds = [
        'https://github.com/minetest/minetest/commits/master.atom', 
        'https://github.com/mintest/minetest_game/commits/master.atom',
        'https://github.com/Uberi/MineTest-WorldEdit/commits/master.atom', 
        'https://github.com/Jeija/minetest-mod-mesecons/commits/master.atom'
    ]
    for url in feeds:
        options = {
            'agent': 'Mozilla/5.0 (MinetestBot)',
            'referrer': 'http://minetest.net'
        }
        feed = feedparser.parse(url, **options)
        if len(feed.entries) == 0: continue
        last_entry = feed.entries[0]
        feednum = get_arrayindex(feeds,url)
        if not feednum in rssnotify["last_updated_feeds"].keys():
            rssnotify["last_updated_feeds"][feednum] = -1
        if rssnotify["last_updated_feeds"][feednum] != last_entry.updated:
            rssnotify["last_updated_feeds"][feednum] = last_entry.updated
            commiter_realname = last_entry.authors[0].name
            try:
                commiter = last_entry.authors[0].href.replace('https://github.com/',"")
            except AttributeError:
                commiter = commiter_realname # This will only print the Realname if the nickname couldn't be obtained
            reponame = url.replace("https://github.com/","").replace("/commits/master.atom","")
            commit_hash = last_entry.links[0].href.replace("https://github.com/" + reponame + "/commit/","")[:10]
            commit_time = last_entry.updated
            print("[LOG]: Found RSS Update for URL '%s'" % (url))
            if rssnotify["dont_print_first_message"]:
                continue # Don't print first Message
            if rssnotify["show_commit_link"]:
                if rssnotify["use_git.io"]:
                    params = urllib.urlencode({'url' : last_entry.link}) # git.io only works with *.github.com links
                    u = urllib.urlopen("http://git.io/create", params)
                    commit_link = "http://git.io/" + u.read()
                else:
                    commit_link = last_entry.link
            else:               
                commit_link = ""
            
            for ch in phenny.bot.channels:
                if commiter.lower() != commiter_realname.lower():
                    #phenny.say("GIT: %s (%s) commited to %s: %s %s %s" % (commiter,commiter_realname,reponame,last_entry.title,commit_hash,commit_time))
                    phenny.write(['PRIVMSG',ch],"GIT: %s (%s) commited to %s: %s %s %s %s" % (commiter, commiter_realname, reponame, last_entry.title, commit_hash, commit_time, commit_link))
                else:
                    #phenny.say("GIT: %s commited to %s: %s %s %s" % (commiter,reponame,last_entry.title,commit_hash,commit_time))
                    phenny.write(['PRIVMSG',ch],"GIT: %s commited to %s: %s %s %s %s" % (commiter, reponame, last_entry.title, commit_hash, commit_time, commit_link))
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
