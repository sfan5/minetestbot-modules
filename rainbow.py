#!/usr/bin/env python
"""
rainbow.py - Rainbows
Copyright 2013, sfan5
"""
import random

rainbowcolors = ["4", "7", "8", "3", "12", "6", "13"]
#TODO: make this rainbow better (can't really make it that better because IRC colors suck)

def colorize(text):
	out = ""
	i = 0
	for c in text:
		if c in list(str(i) for i in range(10)):
			c = u"\u200b" + c # 'ZERO WIDTH SPACE' cuz IRC clients are stupid
		out += "\x03" + str(rainbowcolors[i]) + c
		i += 1
		if i >= len(rainbowcolors):
			i = 0
	return out

def rainbow(phenny, input):
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return # Abort function
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
