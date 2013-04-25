#!/usr/bin/env python
"""
server.py - Phenny Minetest Server Module
Copyright 2012, Sfan5
"""

import web, json, random

def read_server():
   text = web.get("http://servers.minetest.net/list")
   server_list = json.loads(text)["list"]
   choice = random.randrange(0, len(server_list))

   name = server_list[choice]["name"]
   address = server_list[choice]["address"]
   clients = server_list[choice]["clients"]
   version = server_list[choice]["version"]
   ping = server_list[choice]["ping"]
   clients_top = server_list[choice]["clients_top"]

   return "%s | %s | Clients: %s/%s | Version: %s | ping: %s" % (name, address, clients, clients_top, version, ping)

def server(phenny, input):
   for x in phenny.bot.commands["high"].values():
     if x[0].__name__ == "aa_hook":
        if x[0](phenny, input):
           return # Abort function
   phenny.reply(read_server())

server.commands = ['sv', 'server']
server.thread = True

if __name__ == '__main__':
   print __doc__
