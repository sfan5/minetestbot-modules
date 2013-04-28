#!/usr/bin/env python
"""
chop.py - Phenny Channel Administration Module
Copyright 2013, Sfan5
"""
import os

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
