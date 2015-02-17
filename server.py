#!/usr/bin/env python
"""
server.py - Phenny Minetest Server Module
Copyright 2013, sfan5
Licensed under GNU General Public License v2.0
"""

import web, random

def by_random(tbl, arg):
    return [random.randrange(0, len(tbl))]

def create_stringcompare(name, substring=True):
  def m(tbl, arg):
      results = []
      for i in range(0, len(tbl)):
          e = tbl[i]
          if substring and arg.lower() in e[name].lower():
              results.append(i)
          elif not substring and arg.lower().strip() == e[name].lower().strip():
              results.append(i)
      return results
  return m

def create_intcompare(name, most_least=True):
  def m(tbl, arg):
      results = []
      if arg.startswith("<"): # less comparing
          try:
              nu = float(arg[1:])
          except:
              return []
          for i in range(0, len(tbl)):
              if tbl[i][name] < nu:
                  results.append(i)
      elif arg.startswith(">"): # more comparing
          try:
              nu = float(arg[1:])
          except:
              return []
          for i in range(0, len(tbl)):
              if tbl[i][name] > nu:
                  results.append(i)
      elif arg == "most" and most_least: # most
          ranking = (-1, None)
          for i in range(0, len(tbl)):
              if tbl[i][name] > ranking[0]:
                  ranking = (tbl[i][name], i)
          results.append(ranking[1])
      elif arg == "least" and most_least: # least
          ranking = (2**32, None)
          for i in range(0, len(tbl)):
              if tbl[i][name] < ranking[0]:
                  ranking = (tbl[i][name], i)
          results.append(ranking[1])
      elif arg.startswith("!"): # not comparing
          try:
              nu = float(arg[1:])
          except:
              return []
          for i in range(0, len(tbl)):
              if int(tbl[i][name]) != nu:
                  results.append(i)
      else:
          if arg.startswith("="): # support "3" and "=3"
              arg = arg[1:]
          try:
              nu = float(arg)
          except:
              return []
          for i in range(0, len(tbl)):
              if int(tbl[i][name]) == nu:
                  results.append(i)
      return results
  return m

def by_index(tbl, arg):
    if arg == "last":
        return [len(tbl) - 1]
    else:
        try:
            if int(arg) < len(tbl) - 1:
                return [int(arg)]
        except:
            return []

compare_methods = {
  "addr": create_stringcompare("address"),
  "name": create_stringcompare("name"),
  "players": create_intcompare("clients"),
  "ping": create_intcompare("ping"),
  "port": create_intcompare("port", most_least=False),
  "i": by_index,
}

default_method = "name"

def server(phenny, input):
    arg = input.group(2)
    if not arg:
        cmds = [(by_random, "")]
    else:
        arg = arg.strip().split(" ")
        cmds = []
        for a in arg:
            choicefunc = None
            for mname in compare_methods:
              if a.lower().startswith(mname + ":"):
                choicefunc = compare_methods[mname]
                carg = a[len(mname + ":"):]
                break
            if a.lower() == "random":
                choicefunc = by_random
                carg = ""
            elif not choicefunc:
                choicefunc = compare_methods[default_method]
                carg = a
            cmds.append((choicefunc, carg))

    text, sc = web.get("http://servers.minetest.net/list")
    text = str(text, 'utf-8')
    server_list = web.json(text)["list"]
    prep_table = server_list
    for i in range(0, len(cmds)):
        choicefunc, carg = cmds[i]
        choices = choicefunc(prep_table, carg)
        if len(choices) == 0:
            return phenny.reply("No results")
        prep_table = list(prep_table[c] for c in choices)

    choice = prep_table[0]
    name = choice["name"]
    address = choice["address"]
    if choice["port"] != 30000:
        if ':' in address: # IPv6
            address = "[" + address + "]"
        address += ":" + str(choice["port"])
    clients = choice["clients"]
    if "gameid" in choice:
        version = choice["version"] + " / " + choice["gameid"]
    else:
        version = choice["version"]
    ping = int(choice["ping"] * 1000)
    clients_max = choice["clients_max"]
    clients_avg = choice["pop_v"]
    clients_top = choice["clients_top"]

    phenny.reply("%s | %s | Clients: %d/%d, %d/%d | Version: %s | Ping: %dms" % (name, address, clients, clients_max, clients_avg, clients_top, version, ping))

server.commands = ['sv', 'server']

if __name__ == '__main__':
   print(__doc__)
