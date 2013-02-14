#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Modified by Sfan5 2013
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
from tools import deprecated

def seen(phenny, input): 
   """.seen <nick> - Reports when <nick> was last seen."""
   for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
   nick = input.group(2)
   if not nick:
      return phenny.reply("Need a nickname to search for...")
   nick = nick.lower()
   
   print("[LOG]: %s queried Seen Result for %s" % (input.nick,nick))
   if not hasattr(phenny, 'seen'): 
      return phenny.reply("?")

   if phenny.seen.has_key(nick): 
      channel, t = phenny.seen[nick]
      t = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(t))

      msg = "%s was last seen at %s on %s" % (nick, t, channel)
      phenny.reply(msg)
   else: phenny.reply("Sorry, I haven't seen %s around." % nick)
seen.rule = (['seen'], r'(\S+)')

@deprecated
def f_note(self, origin, match, args): 
   def note(self, origin, match, args): 
      if not hasattr(self.bot, 'seen'): 
         self.bot.seen = {}
      if origin.sender.startswith('#'): 
         self.seen[origin.nick.lower()] = (origin.sender, time.time())

   try: note(self, origin, match, args)
   except Exception, e: print e
f_note.rule = r'(.*)'
f_note.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
