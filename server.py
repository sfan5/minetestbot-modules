#!/usr/bin/env python
"""
server.py - Phenny Minetest Server Module
Copyright 2012, Sfan5
"""

import web, json, random

def by_random(tbl, arg):
    return random.randrange(0, len(tbl))

def by_address(tbl, arg):
    for i in range(0, len(tbl)):
        e = tbl[i]
        if arg.lower().strip() in e["address"].lower().strip():
            return i
    return None

def by_name(tbl, arg):
    for i in range(0, len(tbl)):
        e = tbl[i]
        if arg.lower().strip() in e["name"].lower().strip():
            return i
    return None

def by_players(tbl, arg):
    if arg.startswith("<"): # less comparing
        try:
            nu = int(arg[1:])
        except:
            return None
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) < nu:
                return i
    elif arg.startswith(">"): # more comparing
        try:
            nu = int(arg[1:])
        except:
            return None
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) > nu:
                return i
    elif arg == "most": # most
        ranking = (-1, None)
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) > ranking[0]:
                ranking = (tbl[i]["clients"], i)
        return ranking[1]
    elif arg == "least": # least
        ranking = (9999, None)
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) < ranking[0]:
                ranking = (tbl[i]["clients"], i)
        return ranking[1]
    else:
        if arg.startswith("="): # support "3" and "=3"
            arg = arg[1:]
        try:
            nu = int(arg)
        except:
            return None
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) == nu:
                return i
        return nu
    return None

def server(phenny, input):
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function

    arg = input.group(2)
    if not arg:
        choicefunc = by_random
        carg = None
    else:
        if arg.startswith("addr:"):
            choicefunc = by_address
            carg = arg[len("addr:"):]
        elif arg.startswith("name:"):
            choicefunc = by_address
            carg = arg[len("name:"):]
        elif arg.startswith("players:"):
            choicefunc = by_players
            carg = arg[len("players:"):]
        else:
            choicefunc = by_name
            carg = None

    text = web.get("http://servers.minetest.net/list")
    server_list = json.loads(text)["list"]
    choice = choicefunc(server_list, carg)
    if choice == None:
        phenny.reply("No results")

    name = server_list[choice]["name"]
    address = server_list[choice]["address"]
    clients = server_list[choice]["clients"]
    version = server_list[choice]["version"] + " " + server_list[choice]["gameid"]
    ping = server_list[choice]["ping"]
    clients_top = server_list[choice]["clients_top"]

    phenny.reply("%s | %s | Clients: %s/%s | Version: %s | ping: %s" % (name, address, clients, clients_top, version, ping))

server.commands = ['sv', 'server']
server.thread = True

if __name__ == '__main__':
   print __doc__
