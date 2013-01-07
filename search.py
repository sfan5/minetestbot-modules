#!/usr/bin/env python
"""
search.py - Phenny Web Search Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Modified by Sfan5 2012
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import web, re

search_badwords = ["porn","p0rn","pr0n","pron","redtube","sex","pussy","hot","weed","smoking","drug","penis","vagina"] #Thank KikaRz, LandMine and RagnarLaud for this
search_badnicks = ["KikaRz","LandMine","LandMineMT"]

class Grab(web.urllib.URLopener):
   def __init__(self, *args):
      self.version = 'Mozilla/5.0 (MinetestBot)'
      web.urllib.URLopener.__init__(self, *args)
      self.addheader('Referer', 'http://minetest.net')
   def http_error_default(self, url, fp, errcode, errmsg, headers):
      return web.urllib.addinfourl(fp, [headers, errcode], "http:" + url)

def google_ajax(query): 
   """Search using AjaxSearch, and return its JSON."""
   if isinstance(query, unicode): 
      query = query.encode('utf-8')
   uri = 'http://ajax.googleapis.com/ajax/services/search/web'
   args = '?v=1.0&safe=off&q=' + web.urllib.quote(query)
   handler = web.urllib._urlopener
   web.urllib._urlopener = Grab()
   bytes = web.get(uri + args)
   web.urllib._urlopener = handler
   return web.json(bytes)

def google_search(query): 
   results = google_ajax(query)
   try: return results['responseData']['results'][0]['unescapedUrl']
   except IndexError: return None
   except TypeError: 
      print results
      return False

def google_count(query): 
   results = google_ajax(query)
   if not results.has_key('responseData'): return '0'
   if not results['responseData'].has_key('cursor'): return '0'
   if not results['responseData']['cursor'].has_key('estimatedResultCount'): 
      return '0'
   return results['responseData']['cursor']['estimatedResultCount']

def formatnumber(n): 
   """Format a number with beautiful commas."""
   parts = list(str(n))
   for i in range((len(parts) - 3), 0, -3):
      parts.insert(i, ',')
   return ''.join(parts)


def g(phenny, input): 
   """Queries Google for the specified input."""
   query = input.group(2)
   if not query: 
      return phenny.reply('.g what?')
   for bw in search_badwords:
	if bw in query:
		print("[LOG]: %s queried Google Result for '%s' | DENIED: Badword" % (input.nick,query))
		return phenny.reply("Gross!")
   for bn in search_badnicks:
	if bn in input.nick:
		print("[LOG]: %s queried Google Result for '%s' | DENIED: Badnick" % (input.nick,query))
		return phenny.reply("Nope!")
   query = query.encode('utf-8')
   print("[LOG]: %s queried Google Result for '%s'" % (input.nick,query))
   uri = google_search(query)
   if uri: 
      phenny.reply(uri)
      if not hasattr(phenny.bot, 'last_seen_uri'):
         phenny.bot.last_seen_uri = {}
      phenny.bot.last_seen_uri[input.sender] = uri
   elif uri is False: phenny.reply("Problem getting data from Google.")
   else: phenny.reply("No results found for '%s'." % query)
g.commands = ['g']
g.priority = 'high'
g.example = '.g minetest'

def gc(phenny, input):
   if not input.group(2):
      return phenny.reply("No query term.")
   query = input.group(2).encode('utf-8')
   result = new_gc(query)
   for bw in search_badwords:
	if bw in query:
		print("[LOG]: %s queried Google Result Number for '%s' | DENIED: Badword" % (input.nick,query))
		return phenny.reply("Gross!")
   for bn in search_badnicks:
	if bn in input.nick:
		print("[LOG]: %s queried Google Result Number for '%s' | DENIED: Badnick" % (input.nick,query))
		return phenny.reply("Nope!")
   print("[LOG]: %s queried Google Result Number for '%s'" % (input.nick,query))
   if result:
      phenny.say(query + ": " + result)
   else: phenny.reply("Sorry, couldn't get a result.")
   
def new_gc(query):
   uri = 'https://www.google.com/search?hl=en&q='
   uri = uri + web.urllib.quote(query).replace('+', '%2B')
   if '"' in query: uri += '&tbs=li:1'
   bytes = web.get(uri)
   if "did not match any documents" in bytes:
      return "0"
   for result in re.compile(r'(?ims)([0-9,]+) results?').findall(bytes):
      return result
   return None

gc.commands = ['gc']
gc.priority = 'high'
gc.example = '.gc minetest'

if __name__ == '__main__': 
   print __doc__.strip()
