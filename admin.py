#!/usr/bin/env python
"""
admin.py - Phenny Admin Module
Copyright 2008-9, Sean B. Palmer, inamidst.com
Modified by sfan5 2013
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

def join(phenny, input):
   """Join the specified channel. This is an admin-only command."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin:
      channel, key = input.group(1), input.group(2)
      if not key:
         phenny.write(['JOIN'], channel)
      else: phenny.write(['JOIN', channel, key])
join.rule = r'\!join (#\S+)(?: *(\S+))?'
#join.commands = ['join']
join.priority = 'low'
join.example = '.join #example or .join #example key'

def part(phenny, input):
   """Part the specified channel. This is an admin-only command."""
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin:
      if ' ' in input.group(2):
         arg = input.group(2).split(" ")
         arg2 = ' '.join(arg[1:])
         arg = arg[0]
         phenny.write(['PART', arg], arg2)
      else:
         phenny.write(['PART'], input.group(2))
part.commands = ['part']
part.priority = 'low'
part.example = '.part #example'

def quit(phenny, input):
   """Quit from the server. This is an owner-only command."""
   # Can only be done in privmsg by the owner
   if input.sender.startswith('#'): return
   if input.owner:
      phenny.write(['QUIT'])
      __import__('os')._exit(0)
quit.commands = ['quit']
quit.priority = 'low'

def quit2(phenny, input):
    if input.sender.startswith('#'): input.sender = "this_is_not_a_channel" # Allows you to use it in a Channel
    quit(phenny, input)
quit2.rule = ('$nick', 'quit')
quit2.priority = 'low'

def msg(phenny, input):
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   a, b = input.group(2), input.group(3)
   if (not a) or (not b): return
   if input.admin:
      phenny.msg(a, b)
msg.rule = (['msg'], r'(#?\S+) (.+)')
msg.priority = 'low'

def me(phenny, input):
   # Can only be done in privmsg by an admin
   if input.sender.startswith('#'): return
   if input.admin:
      msg = '\x01ACTION %s\x01' % input.group(3)
      phenny.msg(input.group(2) or input.sender, msg)
me.rule = (['me'], r'(#?\S+) (.+)')
me.priority = 'low'

def py(phenny, input):
	if input.owner:
		phenny.say(repr(eval(input.group(2))))
py.commands = ['py']
py.priority = 'high'

if __name__ == '__main__':
   print(__doc__.strip())
