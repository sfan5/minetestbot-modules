#!/usr/bin/env python
"""
rutils.py - Phenny Utility Module
Copyright 2012, Sfan5
"""
import base64, binascii

def rev(phenny, input): 
    """reverse string"""
    if not input.group(2):
        return phenny.reply("Nothing to reverse.")
    q = input.group(2).encode('utf-8')
    s = ""
    for i in range(1,len(q)):
        s += q[-i]
    s += q[0]
    return phenny.say(s)

rev.commands = ['re','rev','reverse']
rev.priority = 'low'

def b64e(phenny, input): 
    """base64 encode"""
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b64encode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b64e.commands = ['b64e','base64encode']
b64e.priority = 'low'

def b64d(phenny, input): 
    """base64 decode"""
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b64decode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b64d.commands = ['b64d','base64decode']
b64d.priority = 'low'

def b32e(phenny, input): 
    """base32 encode"""
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b32encode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b32e.commands = ['b32e','base32encode']
b32e.priority = 'low'

def b32d(phenny, input): 
    """base32 decode"""
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b32decode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b32d.commands = ['b32d','base32decode']
b32d.priority = 'low'

def b16e(phenny, input): 
    """base16 encode"""
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b16encode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b16e.commands = ['b16e','base16encode']
b16e.priority = 'low'

def b16d(phenny, input): 
    """base16 decode"""
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(base64.b16decode(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
b16d.commands = ['b16d','base16decode']
b16d.priority = 'low'

def crc32(phenny, input): 
    """crc32 hash"""
    if not input.group(2):
        return phenny.reply("Nothing to hash.")
    q = input.group(2).encode('utf-8')
    h = binascii.crc32(q)
    return phenny.say(str(h) + "(" + hex(h) + ")")
   
crc32.commands = ['crc32']
crc32.priority = 'low'

def hex_(phenny, input): 
    """hexlify http://docs.python.org/2/library/binascii.html#binascii.hexlify"""
    if not input.group(2):
        return phenny.reply("Nothing to hexlify.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(binascii.hexlify(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
hex_.commands = ['hex']
hex_.priority = 'low'

def unhex(phenny, input): 
    """unhexlify http://docs.python.org/2/library/binascii.html#binascii.unhexlify"""
    if not input.group(2):
        return phenny.reply("Nothing to unhexlify.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(binascii.unhexlify(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
unhex.commands = ['unhex']
unhex.priority = 'low'

def uuencode(phenny, input): 
    """uuencode"""
    if not input.group(2):
        return phenny.reply("Nothing to encode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(binascii.b2a_uu(q))
    except BaseException as e:
        return phenny.reply(e.message)
   
uuencode.commands = ['ue','uuencode']
uuencode.priority = 'low'

def uudecode(phenny, input): 
    """uudecode"""
    if not input.group(2):
        return phenny.reply("Nothing to decode.")
    q = input.group(2).encode('utf-8')
    try:
        return phenny.say(binascii.a2b_uu(q + '\n'))
    except BaseException as e:
        return phenny.reply(e.message)
   
uudecode.commands = ['ud','uudecode']
uudecode.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
