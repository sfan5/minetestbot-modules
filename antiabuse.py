#!/usr/bin/env python
"""
antiabuse.py - Phenny AntiAbuse Module
Copyright 2012, Sfan5
"""
import time

antiabuse = {}
antiabuse["timeout"] = {}
antiabuse["ignorelist"] = ["KikaRz","LandMine","LandMineMT","markveidemanis"]
antiabuse["s_timeout"] = 3 # in Seconds

def aa_hook(phenny, input):
    if input.admin or input.owner:
        return False
    #Ignore-List check
    if input.nick in antiabuse["ignorelist"]:
        return True # abort command
    #Timeout check
    try:
        ot = antiabuse["timeout"][input.nick]
    except:
        ot = 0
    antiabuse["timeout"][input.nick] = time.time()
    if antiabuse["timeout"][input.nick] - antiabuse["s_timeout"] < ot:
        return True # abort command
        pass
    
    return False
aa_hook.event = 'THISWONTHAPPEN'
aa_hook.priority = 'high'
aa_hook.rule = r'h^'
#Warning: Uses a very very dirty hack to achieve that other modules can access this function


def ignore(phenny, input):
    if not input.admin and not input.owner: return
    arg = input.group(2).strip()
    antiabuse["ignorelist"].append(arg)
    phenny.reply("'%s' added to ignore list." % arg)

ignore.commands = ['ignore']
ignore.priority = 'high'

def unignore(phenny, input):
    if not input.admin and not input.owner: return
    arg = input.group(2).strip()
    try:
        antiabuse["ignorelist"].remove(arg)
    except:
        return
    phenny.reply("'%s' removed from ignore list." % arg)

unignore.commands = ['unignore']
unignore.priority = 'high'

