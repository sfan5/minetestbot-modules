#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2014, sfan5
"""

import math
import random
import struct
import multiprocessing

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
	if not input.group(2):
		return phenny.reply("Nothing to calculate.")
	q = input.group(2).encode('ascii', 'ignore')
	if '__' in q:
		return phenny.reply("Sorry, but no double underscores.")
	log.log("event", "%s calculated '%s'" % (log.fmt_user(input), q), phenny)
	o = multiprocessing.Queue()
	def get_result(o, q):
		try:
			o.put(repr(eval(q, {'__builtins__': env}, {})))
		except Exception as e:
			o.put(type(e).__name__ + ": " + str(e))
	proc = multiprocessing.Process(target=get_result, args=(o,q))
	proc.start()
	proc.join(2.0)
	if proc.is_alive():
			proc.terminate()
			if 'math.pow' in q or '**' in q:
				phenny.reply("Kindly go fuck yourself!")
				antiabuse.ignore("*!*" + input.hostmask[input.hostmask.find("@"):])
				log.log("action", "Auto-ignored %s for !c crash attempt" % log.fmt_user(input), phenny)
			else:
				phenny.reply("Took to long to calculate")
			return
	else:
		phenny.say(o.get())


c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__':
	print __doc__.strip()
