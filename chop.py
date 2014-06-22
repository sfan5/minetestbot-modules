#!/usr/bin/env python
"""
chop.py - Phenny Channel Administration Module
Copyright 2013, sfan5
"""
import os, web, re

chop = {}
chop["badword_limit"] = 4
chop["badword_enabled"] = True
chop["badword_kickmsg"] = "Chop!" # "Stop using bad words!"
chop["victims"] = {} # for future use
badword_list = "" # TODO: Get badword list from somewhere

def num_badwords(sentence):
    badwords = 0
    for bwl in badword_list.split("\n"):
        args = bwl.split(" ")
        if len(args) < 2: continue
        arg = ' '.join(args[1:]).rstrip("\n\r")
        if args[0] == "regex":
            try:
                rgx = re.compile(arg)
            except Exception as e:
                print("Error while compiling regex ''%s'': %s" % (arg, str(e)))
                continue
        for word in sentence.split(" "):
            word = word.rstrip(",.;:")
            word = word.lstrip(",.;:")
            if args[0] == "raw":
                if word.lower() == arg.lower():
                    badwords += 1
            elif args[0] == "regex":
                if not rgx.match(word) == None:
                    badwords += 1
        if args[0] == "regex": del rgx

    return badwords

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

def chanmodefunc(phenny, input, mode, modfunc=None):
    if modfunc == None:
        modfunc = lambda x: x
    arg = input.group(2)
    if not arg: return phenny.write(['MODE', input.sender, mode, input.nick], "")
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

def voice(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '+v')

voice.commands = ['voice']

def devoice(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '-v')

devoice.commands = ['devoice']

def op(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '+o')

op.commands = ['op']

def deop(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '-o')

deop.commands = ['deop']

def ban(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '+b', hmasktrans)

ban.commands = ['ban']

def unban(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '-b', hmasktrans)

unban.commands = ['unban']

def mute(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '+q', hmasktrans)

mute.commands = ['mute']

def unmute(phenny, input):
    if not input.admin: return
    chanmodefunc(phenny, input, '-q', hmasktrans)

unmute.commands = ['unmute']

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

def badword_watcher(phenny, input):
    if not input.sender.startswith('#'): return
    if not chop["badword_enabled"]: return
    bwc = num_badwords(input.group(0))
    if bwc > chop["badword_limit"]:
        phenny.write(['KICK', input.sender, input.nick], chop["badword_kickmsg"])
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
        phenny.say("done.")
    elif arg == "disable" or arg == "off":
        chop["badword_enabled"] = False
        phenny.say("done.")
    elif arg == "reload":
        badword_list = "" # TODO: Get badword list from somewhere
        phenny.say("done.")

badword_ctrl.commands = ['badword']
