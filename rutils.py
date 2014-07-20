#!/usr/bin/env python
"""
rutils.py - Phenny Utility Module
Copyright 2012, sfan5
"""
import base64, binascii, re, random, time, multiprocessing, hashlib

def rs(s):
    return repr(s)[1:-1]

def rev(phenny, input):
    """reverse string"""
    if not input.group(2):
        return phenny.reply("Nothing to reverse.")
    q = input.group(2)
    s = ""
    for i in range(1,len(q)):
        s += q[-i]
    s += q[0]
    return phenny.say(rs(s))

rev.commands = ['rev','reverse']
rev.priority = 'low'

def make_thing(cmds, func):
  def m(phenny, input):
    if not input.group(2): return
    q = input.group(2).encode('utf-8')
    try:
        phenny.say(rs(func(q).decode('utf-8')))
    except BaseException as e:
        phenny.reply("Failed to handle data")
  m.commands = cmds
  m.priority = "low"
  return m

b64e = make_thing(['b64e','base64encode'], base64.b64encode)
b64d = make_thing(['b64d','base64decode'], base64.b64decode)
b32e = make_thing(['b32e','base32encode'], base64.b32encode)
b32d = make_thing(['b32d','base32decode'], base64.b32decode)
b16e = make_thing(['b16e','base16encode'], base64.b16encode)
b16d = make_thing(['b16d','base16decode'], base64.b16decode)

def hash_(phenny, input):
	if not input.group(2):
		return phenny.reply("Usage: hash <hash function> <text> | Get available hash funcs with ?")
	hashfuncs = {
		'md5':		hashlib.md5,
		'sha1':		hashlib.sha1,
		'sha224':	hashlib.sha224,
		'sha256':	hashlib.sha256,
		'sha384':	hashlib.sha384,
		'sha512':	hashlib.sha512,
	}
	if input.group(2).strip() == '?':
		return phenny.reply('Supported hash functions: ' + ', '.join(hashfuncs.keys()))
	hashf = input.group(2).split(' ')[0]
	if not hashf in hashfuncs:
		return phenny.reply('Unknown hash functions, supported: ' + ', '.join(hashfuncs.keys()))
	data = ' '.join(input.group(2).split(' ')[1:]).encode('utf-8')
	phenny.say(hashfuncs[hashf](data).hexdigest())

hash_.commands = ['hash']
hash_.priority = 'low'

def rand(phenny, input):
    """Returns a random number"""
    if not input.group(2):
        return
    arg = input.group(2)
    if " " in arg:
        try:
            a = int(arg.split(" ")[0])
        except ValueError:
            return phenny.reply("Could not parse argument 1")
        try:
            b = int(arg.split(" ")[1]) + 1
        except ValueError:
            return phenny.reply("Could not parse argument 2")
        if b < a:
            tmp = a
            a = b
            b = tmp
            del tmp
        phenny.say(str(random.randrange(a, b)))
    else:
        try:
            a = int(arg.split(" ")[0]) + 1
        except ValueError:
            return phenny.reply("Could not parse argument 1")
        phenny.say(str(random.randrange(a)))

rand.commands = ['rand', 'random']
rand.priority = 'low'

if __name__ == '__main__':
   print(__doc__.strip())
