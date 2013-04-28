#!/usr/bin/env python
"""
chop.py - Phenny Channel Administration Module
Copyright 2013, Sfan5
"""
import os, web, re

chop = {}
chop["badword_limit"] = 4
chop["badword_enabled"] = True
chop["victims"] = {} # for future use
badword_list = web.get("http://sfan5.minetest.net/badwords.txt")

def num_badwords(sentence):
    badwords = 0
    for bwl in badword_list.split("\n"):
        arg = bwl.split(" ")
        if len(arg) < 2: continue
        arg[1] = arg[1].rstrip("\n\r")
        if arg[0] == "regex": rgx = re.compile(arg[1])
        for word in sentence.split(" "):
            word = word.rstrip(",.;")
            word = word.lstrip(",.;")
            if arg[0] == "raw":
                if word.lower() == arg[1].lower():
                    badwords += 1
            elif arg[0] == "regex":
                if not rgx.match(word) == None:
                    badwords += 1
        if arg[0] == "regex": del rgx
        
    return badwords

def voice(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        phenny.write(['MODE', input.sender, '+v', va], "")

voice.commands = ['voice']

def devoice(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        phenny.write(['MODE', input.sender, '-v', va], "")

devoice.commands = ['devoice']

def kick(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        phenny.write(['KICK', input.sender, va], "")

kick.commands = ['kick']

def ban(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        a = "!" in va
        b = "@" in va
        if not a and not b:
            phenny.write(['MODE', input.sender, '+b', "*!*" + va + "@*"], "")
        elif a and not b:
            phenny.write(['MODE', input.sender, '+b', va + "@*"], "")
        elif not a and b:
            phenny.write(['MODE', input.sender, '+b', "*!*" + va], "")
        else: # a and b
            phenny.write(['MODE', input.sender, '+b', va], "")

ban.commands = ['ban']

def unban(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        a = "!" in va
        b = "@" in va
        if not a and not b:
            phenny.write(['MODE', input.sender, '-b', "*!*" + va + "@*"], "")
        elif a and not b:
            phenny.write(['MODE', input.sender, '-b', va + "@*"], "")
        elif not a and b:
            phenny.write(['MODE', input.sender, '-b', "*!*" + va], "")
        else: # a and b
            phenny.write(['MODE', input.sender, '-b', va], "")

unban.commands = ['unban']

def op(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        phenny.write(['MODE', input.sender, '+o', va], "")

op.commands = ['op']

def deop(phenny, input):
    if not input.admin: return
    if not input.sender.startswith('#'): return
    # Can only be done in a channel by an admin
    arg = input.group(2)
    if not arg: return
    arg = arg.split(" ")
    for va in arg:
        phenny.write(['MODE', input.sender, '-o', va], "")

deop.commands = ['deop']

def badword_watcher(phenny, input):
    if not input.sender.startswith('#'): return
    if not chop["badword_enabled"]: return
    bwc = num_badwords(input.group(0))
    if bwc > chop["badword_limit"]:
        phenny.write(['KICK', input.sender, input.nick], "CHOP!") #"Stop using badwords!")
        try:
            chop["victims"][input.nick] += 1
        except:
            chop["victims"][input.nick] = 1

badword_watcher.priority = 'high'
badword_watcher.rule = r'.*'

def badword_ctrl(phenny, input):
    if not input.admin: return
    arg = input.group(2)
    if not arg: return
    if arg == "enable" or arg == "on":
        chop["badword_enabled"] = True
    elif arg == "disable" or arg == "off":
        chop["badword_enabled"] = False

badword_ctrl.commands = ['badword']
