#!/usr/bin/env python
"""
shortutil.py - Phenny Custom Shortcut Module
Copyright 2013 jmf
Licensed under the WTFPL.
http://www.wtfpl.net/txt/copying/

Module for phenny:
http://inamidst.com/phenny/
"""

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
	phenny.say("http://is.gd/zgopNT") # http://fc09.deviantart.net/fs70/f/2014/002/d/f/wow_by_kawiku-d70lb8q.png

doge.commands = ['doge']

def catbug(phenny, input):
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return
	phenny.say("http://is.gd/uZNzyW") # http://fc05.deviantart.net/fs70/f/2013/089/b/9/just_one_peanut_butter_square_by_oemilythepenguino-d5zvsem.png

catbug.commands = ['catbug']

