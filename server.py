#!/usr/bin/env python
"""
server.py - Phenny Minetest Server Module
Copyright 2012, Sfan5
"""

import web, math, random
from xml.dom import minidom

def read_server():
   for x in phenny.bot.commands["high"].values():
     if x[0].__name__ == "aa_hook":
        if x[0](phenny, input):
           return # Abort function
   bytes = web.get("http://servers.minetest.ru/")
   shim = '<table>'
   shim2 = '</table>'
   if shim in bytes and shim2 in bytes:
      bytes = bytes.split(shim, 1).pop()
      bytes = bytes.split(shim2, 1)[0]
      bytes = "<table>" + bytes + "</table>" # Root Tag needed
      dom = minidom.parseString(bytes)
      l = dom.getElementsByTagName("tr")
      chosen = l[int(math.floor(random.random()*(len(l)-1))+1)]
      datas = chosen.getElementsByTagName("td")
      name = datas[0].firstChild.data # Server Name
      addr = datas[1].firstChild.data # Server Address
      status = datas[3].firstChild.data # Status (up/down)
      statuspercent = datas[4].firstChild.firstChild.data # Status Percent
      return format(name,addr,status,statuspercent)
   return "Unknown Error"
      

def format(name,addr,status,statuspercent):
	if status == "up":
		return "%s | %s   %s (%s)" % (name,addr,status,statuspercent)
	else:
		return "%s | %s   %s" % (name,addr,status)
def server(phenny, input):
   phenny.reply(read_server())

server.commands = ['sv', 'server']
server.thread = True

if __name__ == '__main__':
   print __doc__
