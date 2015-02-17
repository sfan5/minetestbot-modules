#!/usr/bin/env python
"""
chop.py - Phenny Channel Administration Module
Copyright 2013, sfan5
Licensed under GNU General Public License v2.0
"""

chop = {}

def hmasktrans(va):
    a = "!" in va
    b = "@" in va
    if not a and not b:
        return va + "!*@*"
    elif a and not b:
        return va + "@*"
    elif not a and b:
        return "*!" + va
    else: # a and b
        return va

def chanmodefunc(phenny, input, mode, modfunc=None, notself=False):
    if modfunc == None:
        modfunc = lambda x: x
    arg = input.group(2)
    if not arg:
    	if notself:
    		return phenny.reply("Too few arguments")
    	else:
    		return phenny.write(['MODE', input.sender, mode, input.nick], "")
    arg = arg.split(" ")
    skip_next = False
    for i in range(0, len(arg)):
        if skip_next:
            skip_next = False
            continue
        va = arg[i]
        if va.startswith('#'):
            if i+2 > len(arg): return phenny.reply("Too few arguments")
            phenny.write(['MODE', va, mode, modfunc(arg[i+1])], "")
            skip_next = True
            continue
        phenny.write(['MODE', input.sender, mode, modfunc(va)], "")

def make_thing(command, mode, modfunc=None, notself=False):
	def m(phenny, input):
		if not input.admin: return
		chanmodefunc(phenny, input, mode, modfunc, notself)
	m.commands = [command]
	return m

voice = make_thing("voice", "+v")
devoice = make_thing("devoice", "-v")
op = make_thing("op", "+o")
deop = make_thing("deop", "-o")
ban = make_thing("ban", "+b", hmasktrans, True)
unban = make_thing("unban", "-b", hmasktrans, True)
mute = make_thing("mute", "+q", hmasktrans, True)
unmute = make_thing("unmute", "-q", hmasktrans, True)


def kick(phenny, input):
    if not input.admin: return
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    if len(arg) < 1: return
    if len(arg) == 1:
        arg.append("")
    if arg[0].startswith('#'):
        if len(arg) < 2: return
        phenny.write(['KICK', arg[0], arg[1]], ' '.join(arg[2:]))
    else:
        phenny.write(['KICK', input.sender, arg[0]], ' '.join(arg[1:]))

kick.commands = ['kick']

