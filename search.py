#!/usr/bin/env python
"""
search.py - Phenny Web Search Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Modified by sfan5 2012
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import web
import re

def google_ajax(query):
   """Search using AjaxSearch, and return its JSON."""
   uri = 'http://ajax.googleapis.com/ajax/services/search/web'
   args = '?v=1.0&safe=off&q=' + web.urlencode(query)
   data, sc = web.get(uri + args)
   data = str(data, 'utf-8')
   return web.json(data)

def google_search(query):
   results = google_ajax(query)
   try: return results['responseData']['results'][0]['unescapedUrl']
   except IndexError: return None
   except TypeError:
      return False

def g(phenny, input):
   """Queries Google for the specified input."""
   query = input.group(2)
   if not query:
      return phenny.reply('.g what?')
   log.log("event", "%s searched Google for '%s'" % (log.fmt_user(input), query), phenny)
   uri = google_search(query)
   if uri:
      phenny.reply(uri)
      phenny.bot.last_seen_uri = uri
   elif uri is False: phenny.reply("Problem getting data from Google.")
   else: phenny.reply("No results found for '%s'." % query)
g.commands = ['g']
g.priority = 'high'
g.example = '.g minetest'

def gc(phenny, input):
   query = input.group(2)
   if not query:
      return phenny.reply("No query term.")
   log.log("event", "%s searched Google for '%s'" % (log.fmt_user(input), query), phenny)
   result = new_gc(query)
   if result:
      phenny.say(query + ": " + result)
   else: phenny.reply("Sorry, couldn't get a result.")

def new_gc(query):
   uri = 'https://www.google.com/search?hl=en&q='
   uri = uri + web.urlencode(query).replace('+', '%2B')
   if '"' in query: uri += '&tbs=li:1'
   data, sc = web.get(uri)
   data = str(data, 'utf-8')
   if "did not match any documents" in data:
      return "0"
   for result in re.compile(r'(?ims)([0-9,]+) results?').findall(data):
      return result
   return None

gc.commands = ['gc']
gc.priority = 'high'
gc.example = '.gc minetest'

if __name__ == '__main__':
   print(__doc__.strip())
