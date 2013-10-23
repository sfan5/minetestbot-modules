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
   phenny.say("Somebody thinks you should read the manual. The wiki for dev related questions is at http://dev.minetest.net , the regular wiki is at http://wiki.minetest.net. ")

rtfm.commands = ['rtfm']

def questions(phenny, input):
   """Ask smart questions"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return
   phenny.say("Someone thinks that your question is inaccurate or doesn't follow the guidelines. Read here how to make it right: http://catb.org/~esr/faqs/smart-questions.html")

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
   phenny.say("Someone thinks you need to brush up on or learn Lua, please go to: http://lua.org/pil/")

pil.commands = ['pil']
