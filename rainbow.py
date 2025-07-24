#!/usr/bin/env python
"""
rainbow.py - Rainbows
Copyright 2013, sfan5
Licensed under GNU General Public License v2.0
"""
import random

rainbowcolors = ["4", "7", "8", "3", "12", "6", "13"]

def colorize(text, cyclelen=3):
	if cyclelen == -1: # Auto-detect
		if len(text) < 6:
			cyclelen = 1
		elif len(text) < 13:
			cyclelen = 2
		elif len(text) < 25:
			cyclelen = 3
		else:
			cyclelen = 4
	out = ""
	i = 0
	j = 0
	for c in text:
		if j == 0:
			if c.isdigit():
				c = u"\u200b" + c # 'ZERO WIDTH SPACE' cuz IRC clients are stupid
			out += "\x03" + str(rainbowcolors[i])
		out += c
		j += 1
		if j >= cyclelen:
			i += 1
			j = 0
		if i >= len(rainbowcolors):
			i = 0
	return out

def rainbow(phenny, input):
	arg = input.group(2)
	if not arg:
		return phenny.say(colorize("Rainbow", cyclelen=1) + "\x03 What?")
	if arg.startswith("#") and ' ' in arg and input.admin:
		ch = arg.split(" ")[0]
		arg = " ".join(arg.split(" ")[1:])
		phenny.write(['PRIVMSG', ch], colorize(arg, cyclelen=-1))
	else:
		phenny.say(colorize(arg, cyclelen=-1))

rainbow.commands = ['rainbow']
