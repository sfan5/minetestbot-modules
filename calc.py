#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2014, sfan5
"""

import math
import random
import struct

class SomeObject(object):
	pass

env = {
	"bin": bin, "abs": abs, "oct": oct, "int": int, "sum": sum,
	"tuple": tuple, "divmod": divmod, "hash": hash, "hex": hex,
	"len": len, "list": list, "long": long, "max": max,
	"range": range, "round": round, "min": min, "map": map,
	"zip": zip, "xrange": xrange, "unicode": unicode,
	"unichr": unichr, "type": type, "slice": slice, "ord": ord,
	"chr": chr, "str": str, "float": float
}

libs = [
	'math', 'random', 'struct'
]

for lib in libs:
	env[lib] = SomeObject()
	for funcn in dir(globals()[lib]):
		if funcn.startswith("_"):
			continue
		setattr(env[lib], funcn, getattr(globals()[lib], funcn))

def c(phenny, input):
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return # Abort function
	if not input.group(2):
		return phenny.reply("Nothing to calculate.")
	q = input.group(2).encode('ascii', 'ignore')
	if '__' in q:
		return phenny.reply("Sorry, but no double underscores.")
	print("[LOG]: %s calculated '%s'" % (input.nick, q))
	try:
		phenny.say(repr(eval(q, {'__builtins__': env}, {})))
	except Exception as e:
		phenny.say(type(e).__name__ + ": " + str(e))

c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__': 
	print __doc__.strip()
