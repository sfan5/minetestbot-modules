#!/usr/bin/env python
"""
rainbow.py - Rainbows
Copyright 2013, sfan5
"""
import random

rainbowcolors = ["4", "7", "8", "3", "12", "6", "13"]
#maybe TODO: make this rainbow better (can't really make it that better because IRC colors suck)

def colorize(text):
	out = ""
	i = 0
	j = 0
	for c in text:
		if c in list(str(i) for i in range(10)):
			c = u"\u200b" + c # 'ZERO WIDTH SPACE' cuz IRC clients are stupid
		out += "\x03" + str(rainbowcolors[i]) + c
		j += 1
		if j >= 3:
			i += 1
			j = 0
		if i >= len(rainbowcolors):
			i = 0
	return out

def rainbow(phenny, input):
	arg = input.group(2)
	if not arg:
		return phenny.say(colorize("Rainbow") + "\x03 What?")
	if arg.startswith("#") and ' ' in arg and input.admin:
		ch = arg.split(" ")[0]
		arg = " ".join(arg.split(" ")[1:])
		phenny.write(['PRIVMSG', ch], colorize(arg))
	else:
		phenny.say(colorize(arg))

rainbow.commands = ['rainbow']
