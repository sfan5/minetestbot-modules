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
import urllib2
import json

def rtfm(phenny, input):
   """Manual reference command"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks you should read the manual. The wiki for dev related questions is at http://dev.minetest.net , the regular wiki is at http://wiki.minetest.net. ")

rtfm.commands = ['rtfm']

def questions(phenny, input):
   """Ask smart questions"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks that your question is inaccurate or doesn't follow the guidelines. Read here how to make it right: http://catb.org/~esr/faqs/smart-questions.html")

questions.commands = ['questions']

def next(phenny, input):
   """Next one please"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   phenny.say("Another satisfied customer. Next!")

next.commands = ['next']

def pil(phenny, input):
   """Lua Manual link"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks you need to brush up on or learn Lua, please go to: http://lua.org/pil/")

pil.commands = ['pil']

def git(phenny, input):
   """Git Manual link"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks you need to brush up on or learn Git, please go to: http://git-scm.com/book/")

git.commands = ['git']

def stfu(phenny, input):
   """usage: !stfu [nick]"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks you need to shut the fuck up before you get muted.")

stfu.commands = ['stfu']

def proc(phenny, input):
   """usage: !proc [nick]"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   if input.group(2):
      u = input.group(2).strip() + ", "
   else:
      u = ""
   phenny.say(u + "someone thinks you need to stop procrastinating.")

proc.commands = ['proc']

def doge(phenny, input):
	"""much wow, very function, such programming"""
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return
	if random.randint(0, 1) == 0:
		f = urllib2.urlopen('http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=132')
		data = f.read()
		f.close()
		data = json.loads(data)
		phenny.say("DOGE is at " + data['return']['markets']['DOGE']['lasttradeprice'] + " BTC")
	else:
		phenny.say("http://is.gd/zgopNT") # http://fc09.deviantart.net/fs70/f/2014/002/d/f/wow_by_kawiku-d70lb8q.png

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


