#!/usr/bin/env python
# coding=utf-8
"""
calc.py - Phenny Calculator Module
Copyright 2014, sfan5
"""

import ast
import operator as op
import math

# http://stackoverflow.com/questions/2371436/evaluating-a-mathematical-expression-in-a-string/9558001#9558001
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Pow: op.pow,
			 ast.Div: op.truediv, ast.BitXor: op.xor, ast.Mod: op.mod}

funcs = {"bin": bin, "abs": abs, "oct": oct, "int": int}

for funcn in dir(math):
	if funcn.startswith("__"):
		continue
	funcs[funcn] = getattr(math, funcn)

def getfunc(fn):
	if fn in funcs:
		return funcs[fn]
	else:
		raise ValueError("Function not allowed: '" + str(fn) + "'")

def eval_expr(expr):
	return eval_(ast.parse(expr).body[0].value) # Module(body=[Expr(value=...)])

def eval_(node):
	if isinstance(node, ast.Num): # <number>
		return node.n
	elif isinstance(node, ast.operator): # <operator>
		return operators[type(node)]
	elif isinstance(node, ast.BinOp): # <left> <operator> <right>
		return eval_(node.op)(eval_(node.left), eval_(node.right))
	elif isinstance(node, ast.Call): # <func> ( <args> )
		return getfunc(node.func.id)(*(eval_(e) for e in node.args))
	elif isinstance(node. ast.Tuple): # ( <arg> , <arg2> , [...] )
		return tuple(eval_(e) for e in node.elts)
	elif isinstance(node. ast.List): # [ <arg> , <arg2> , [...] ]
		return list(eval_(e) for e in node.elts)
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
	print("[LOG]: %s calculated '%s'" % (input.nick,q))
	try:
		phenny.say(repr(eval_expr(q)))
	except Exception as e:
		phenny.say("Exception: " + str(e))

c.commands = ['c']
c.example = '.c 5 + 3'

if __name__ == '__main__': 
	print __doc__.strip()
