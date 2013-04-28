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
                ranking = (int(tbl[i]["clients"]), i)
        return ranking[1]
    elif arg == "least": # least
        ranking = (9999, None)
        for i in range(0, len(tbl)):
            if int(tbl[i]["clients"]) < ranking[0]:
                ranking = (int(tbl[i]["clients"]), i)
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

def by_ping(tbl, arg):
    if arg.startswith("<"): # less comparing
        try:
            nu = float(arg[1:])
        except:
            return None
        for i in range(0, len(tbl)):
            if float(tbl[i]["ping"]) < nu:
                return i
    elif arg.startswith(">"): # more comparing
        try:
            nu = int(arg[1:])
        except:
            return None
        for i in range(0, len(tbl)):
            if float(tbl[i]["ping"]) > nu:
                return i
    elif arg == "most": # most
        ranking = (-1, None)
        for i in range(0, len(tbl)):
            if float(tbl[i]["ping"]) > ranking[0]:
                ranking = (float(tbl[i]["ping"]), i)
        return ranking[1]
    elif arg == "least": # least
        ranking = (9999, None)
        for i in range(0, len(tbl)):
            if float(tbl[i]["ping"]) < ranking[0]:
                ranking = (float(tbl[i]["ping"]), i)
        return ranking[1]
    else:
        if arg.startswith("="): # support "0.6" and "=0.6"
            arg = arg[1:]
        try:
            nu = float(arg)
        except:
            return None
        for i in range(0, len(tbl)):
            if float(tbl[i]["clients"]) == nu:
                return i
        return nu
    return None

def by_index(tbl, arg):
    if arg == "last":
        return len(tbl) - 1
    else:
        try:
            return int(arg)
        except:
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
        elif arg.startswith("ping:"):
            choicefunc = by_ping
            carg = arg[len("ping:"):]
        elif arg.startswith("i:"):
            choicefunc = by_index
            carg = arg[len("i:"):]
        else:
            choicefunc = by_name
            carg = None

    text = web.get("http://servers.minetest.net/list")
    server_list = json.loads(text)["list"]
    choice = choicefunc(server_list, carg)
    if choice == None:
        return phenny.reply("No results")

    name = server_list[choice]["name"]
    address = server_list[choice]["address"] + ":" + server_list[choice]["port"]
    clients = server_list[choice]["clients"]
    try:
        version = server_list[choice]["version"] + " " + server_list[choice]["gameid"]
    except:
        version = server_list[choice]["version"]
    ping = server_list[choice]["ping"]
    clients_max = server_list[choice]["clients_max"]

    phenny.reply("%s | %s | Clients: %s/%s | Version: %s | ping: %s" % (name, address, clients, clients_max, version, ping))

server.commands = ['sv', 'server']
server.thread = True

if __name__ == '__main__':
   print __doc__
