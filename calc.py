#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2014, sfan5
"""

import ast
import operator as op
import math
import random

# http://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string/9558001#9558001
operators = {
	ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Pow: op.pow,
	ast.Div: op.truediv, ast.BitXor: op.xor, ast.Mod: op.mod
}

funcs = {
	"bin": bin, "abs": abs, "oct": oct, "int": int, "sum": sum,
	"tuple": tuple, "divmod": divmod, "hash": hash, "hex": hex,
	"len": len, "list": list, "long": long, "max": max,
	"range": range, "round": round, "min": min, "map": map,

	# random functions
	"betavariate": random.betavariate, "choice": random.choice,
	"expovariate": random.expovariate, "gammavariate": random.gammavariate,
	"gauss": random.gauss, "getrandbits": random.getrandbits, 
	"lognormvariate": random.lognormvariate, "normalvariate": random.normalvariate,
	"paretovariate": random.paretovariate, "randint": random.randint,
	"random": random.random, "randrange": random.randrange,
	"sample": random.sample, "shuffle": random.shuffle,
	"triangular": random.triangular, "uniform": random.uniform,
	"vonmisesvariate": random.vonmisesvariate, "weibullvariate": random.weibullvariate
}

for funcn in dir(math):
	if funcn.startswith("_"):
		continue
	funcs[funcn] = getattr(math, funcn)

def getfunc(fn):
	if fn in funcs:
		return funcs[fn]
	else:
		raise ValueError("Function not known: '" + str(fn) + "'")

def get_kwargs(kwrds):
	kwargs = {}
	for kw in kwrds:
		kwargs[kw.arg] = eval_astnode(kw.value)
	return kwargs

def eval_strexpr(expr):
	return eval_astnode(ast.parse(expr).body[0].value) # Module(body=[Expr(value=...)])

def eval_astnode(node):
	if isinstance(node, ast.Num): # <number>
		return node.n
	elif isinstance(node, ast.operator): # <operator>
		return operators[type(node)]
	elif isinstance(node, ast.BinOp): # <left> <operator> <right>
		return eval_astnode(node.op)(eval_astnode(node.left), eval_astnode(node.right))
	elif isinstance(node, ast.Call): # <func> ( <args> )
		return getfunc(node.func.id)(*(eval_astnode(e) for e in node.args), **get_kwargs(node.keywords))
	elif isinstance(node, ast.Tuple): # ( <elem> , <elem2> , [...] )
		return tuple(eval_astnode(e) for e in node.elts)
	elif isinstance(node, ast.List): # [ <elem> , <elem2> , [...] ]
		return list(eval_astnode(e) for e in node.elts)
	elif isinstance(node, ast.Str): # ('|") <text> ('|")
		return node.s
	else:
		raise TypeError("AST node type not allowed: '" + type(node).__name__ + "'")

def c(phenny, input):
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return # Abort function
	if not input.group(2):
		return phenny.reply("Nothing to calculate.")
	q = input.group(2).encode('utf-8')
	print("[LOG]: %s calculated '%s'" % (input.nick, q))
	try:
		phenny.say(repr(eval_strexpr(q)))
	except Exception as e:
		phenny.say("Exception: " + str(e))

c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__': 
	print __doc__.strip()
