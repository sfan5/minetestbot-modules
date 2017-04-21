#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2014, sfan5
Licensed under GNU General Public License v2.0
"""

import math
import random
import struct
import multiprocessing
from functools import reduce

class SomeObject(object):
	pass

env = {
	"abs": abs, "all": all, "any": any,
	"ascii": ascii, "bin": bin, "bool": bool,
	"bytearray": bytearray, "bytes": bytes,
	"callable": callable, "chr": chr,
	"complex": complex, "dict": dict,
	"divmod": divmod, "enumerate": enumerate,
	"filter": filter, "float": float,
	"format": format, "frozenset": frozenset,
	"hex": hex, "int": int,
	"iter": iter, "len": len, "list": list,
	"map": map, "max": max, "min": min,
	"next": next,"oct": oct,
	"ord": ord, "pow": pow, "range": range,
	"reduce": reduce, "repr": repr,
	"reversed": reversed, "round": round,
	"set": set, "slice": slice,
	"sorted": sorted, "str": str,
	"sum": sum, "tuple": tuple,
	"type": type, "zip": zip,
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
	q = input.group(2)
	if '__' in q:
		return phenny.reply("Sorry, double underscores are not allowed.")
	log.log("event", "%s calculated '%s'" % (log.fmt_user(input), q), phenny)
	o = multiprocessing.Queue()
	def get_result(o, q):
		try:
			o.put(repr(eval(q, {'__builtins__': env}, {})))
		except Exception as e:
			o.put(type(e).__name__ + ": " + str(e))
	proc = multiprocessing.Process(target=get_result, args=(o,q))
	proc.start()
	proc.join(3.0)
	if proc.is_alive():
		proc.terminate()
		log.log("action", "Calculation by %s timed out." % log.fmt_user(input), phenny)
		phenny.reply("Took to long to calculate")
	else:
		phenny.say(o.get())


c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__':
	print(__doc__.strip())
