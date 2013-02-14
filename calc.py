#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2008, Sean B. Palmer, inamidst.com
Modified by Sfan5 2012
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import re
import web

r_result = re.compile(r'(?i)<A NAME=results>(.*?)</A>')
r_tag = re.compile(r'<\S+.*?>')

subs = [
   (' in ', ' -> '), 
   (' over ', ' / '), 
   (u'£', 'GBP '), 
   (u'€', 'EUR '), 
   ('\$', 'USD '), 
   (r'\bKB\b', 'kilobytes'), 
   (r'\bMB\b', 'megabytes'), 
   (r'\bGB\b', 'kilobytes'), 
   ('kbps', '(kilobits / second)'), 
   ('mbps', '(megabits / second)')
]

def c(phenny, input): 
   """Google calculator."""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return # Abort function
   if not input.group(2):
      return phenny.reply("Nothing to calculate.")
   q = input.group(2).encode('utf-8')
   q = q.replace('\xcf\x95', 'phi') # utf-8 U+03D5
   q = q.replace('\xcf\x80', 'pi') # utf-8 U+03C0
   print("[LOG]: %s calculated '%s'" % (input.nick,q))
   uri = 'http://www.google.com/ig/calculator?q='
   bytes = web.get(uri + web.urllib.quote(q))
   parts = bytes.split('",')
   answer = [p for p in parts if p.startswith('rhs: "')][0][6:]
   if answer: 
      answer = answer.decode('unicode-escape')
      answer = ''.join(chr(ord(c)) for c in answer)
      answer = answer.decode('utf-8')
      answer = answer.replace(u'\xc2\xa0', ',')
      answer = answer.replace('<sup>', '^(')
      answer = answer.replace('</sup>', ')')
      answer = web.decode(answer)
      phenny.say(answer)
   else: phenny.say('Sorry, no result.')
c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__': 
   print __doc__.strip()
