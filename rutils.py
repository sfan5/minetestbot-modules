#!/usr/bin/env python
"""
rutils.py - Phenny Utility Module
Copyright 2012, sfan5
Licensed under GNU General Public License v2.0
"""
import base64
import random

def rs(s):
    return repr(s)[1:-1]

def make_thing(cmds, func):
  def m(phenny, input):
    if not input.group(2): return
    q = input.group(2).encode('utf-8')
    try:
        phenny.say(rs(func(q).decode('utf-8')))
    except BaseException as e:
        phenny.reply("Failed to handle data")
  m.commands = cmds
  m.priority = "low"
  return m

b64e = make_thing(['b64e','base64encode'], base64.b64encode)
b64d = make_thing(['b64d','base64decode'], base64.b64decode)

def rand(phenny, input):
    """Returns a random number"""
    arg = input.group(2)
    if not arg:
        return
    if " " in arg:
        try:
            a = int(arg.split(" ")[0], base=0)
        except ValueError:
            return phenny.reply("Could not parse first argument")
        try:
            b = int(arg.split(" ")[1], base=0) + 1
        except ValueError:
            return phenny.reply("Could not parse second argument")
        if b < a:
            a, b = b, a
        phenny.say(str(random.randrange(a, b)))
    else:
        try:
            a = int(arg.split(" ")[0], base=0) + 1
        except ValueError:
            return phenny.reply("Could not parse first argument")
        phenny.say(str(random.randrange(a)))

rand.commands = ['rand', 'random']
rand.priority = 'low'

if __name__ == '__main__':
   print(__doc__.strip())
