#!/usr/bin/env python
"""
shortutil.py - Phenny Custom Shortcut Module
Copyright 2013 jmf
Licensed under the WTFPL.
http://www.wtfpl.net/txt/copying/

Module for phenny:
http://inamidst.com/phenny/
"""

import random
import web

def make_cmd(cmd, txt):
  def m(phenny, input):
    t = txt
    if input.group(2):
      u = input.group(2).strip() + ", "
      t = t[0].upper() + t[1:]
    else:
      u = ""
    phenny.say(u + t)
  m.commands = [cmd]
  return m

rtfm = make_cmd("rtfm", "someone thinks you should read the manual. The development wiki is at http://dev.minetest.net, the regular wiki is at http://wiki.minetest.net.")
questions = make_cmd("questions", "someone thinks that your question is inaccurate or doesn't follow the guidelines. Read the guidelines here: http://catb.org/~esr/faqs/smart-questions.html")
pil = make_cmd("pil", "someone thinks you need to brush up on or learn Lua, please go to: http://lua.org/pil/")
git = make_cmd("git", "someone thinks you need to brush up on or learn Git, please go to: http://git-scm.com/book/")
stfu = make_cmd("stfu", "someone thinks you need to shut the fuck up before you get muted.")
proc = make_cmd("proc", "someone thinks you need to stop procrastinating.")

def next(phenny, input):
   """Next one please"""
   phenny.say("Another satisfied customer. Next!")

next.commands = ['next']

def doge(phenny, input):
	"""much wow, very function, such programming"""
	if random.randint(0, 1) == 0:
		data, sc = web.get('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
		data = web.json(data)
		phenny.say("DOGE is at " + data['return']['markets']['DOGE']['lasttradeprice'] + " BTC")
	else:
		links = [
			"http://is.gd/zgopNT", # http://fc09.deviantart.net/fs70/f/2014/002/d/f/wow_by_kawiku-d70lb8q.png
			"http://i.imgur.com/JphfPur.jpg",
			"http://i.imgur.com/2MmvpGR.jpg",
			"https://people.mozilla.org/~smartell/meme/such-logo.gif",
			"http://i.imgur.com/e16WWlK.gif",
			"http://i.imgur.com/6wx9Mf9.png",
			"http://i.imgur.com/1GVIKve.jpg",
			"http://i.imgur.com/606BPbS.png",
			"http://i.imgur.com/VcwHcBO.jpg",
			"http://i.imgur.com/3pnQciA.jpg",
			"http://i.imgur.com/ampdE1n.jpg",
			"http://i.imgur.com/QIqDXZw.gif",
			"http://i.imgur.com/PoYoFXg.jpg",
			"http://i.imgur.com/xcrvGLn.jpg",
			"http://25.media.tumblr.com/282b439e00e13be63e932425388afa7d/tumblr_muopr4oEjG1qbhxqdo1_1280.jpg",
			"http://i.imgur.com/EW37mvz.jpg",
			"http://i.imgur.com/F2vYL4j.gif",
			"http://25.media.tumblr.com/5b1de230c236cbc6310ae000e1a5cdc2/tumblr_mu7uxmD9i31rdj00zo1_500.jpg",
			"http://i.imgur.com/Ck3qYFb.jpg",
			"http://i.imgur.com/wp9x7GY.gif",
			"https://pp.vk.me/c607929/v607929263/624e/K6NMxz0Cj7U.jpg",
			"http://i.imgur.com/q7VKiiK.gif",
			"http://i.imgur.com/RKHNg3v.jpg",
			"http://i.imgur.com/l0YSsre.jpg",
			"http://i.imgur.com/YRdsSHn.jpg",
			"http://i.imgur.com/HhjNnIX.png",
			"http://i.imgur.com/qLbktNN.jpg",
			"http://i.imgur.com/NOIyL1K.jpg",
			"http://i.imgur.com/v7gjzme.jpg",
			"http://i.imgur.com/uI51MQy.png",
			"http://i.imgur.com/JBXo2M5.jpg",
		]
		# ^ How to be productive on a Saturday
		phenny.say(random.choice(links))

doge.commands = ['doge']

def btc(phenny, input):
	"""Get current Bitcoin price"""
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return
	f = urllib2.urlopen('https://blockchain.info/ticker')
	data = f.read()
	f.close()
	data = json.loads(data)
	if input.group(2):
		currency = input.group(2).strip().upper()
	else:
		currency = 'USD'
	if not currency in data.keys():
		return phenny.reply('Unknown currency. Supported currencies: ' + ', '.join(data.keys()))
	phenny.say('1 BTC = %.4f %s' % (data[currency]['15m'], data[currency]['symbol']))

btc.commands = ['btc']
