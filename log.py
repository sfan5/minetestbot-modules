#!/usr/bin/env python
"""
log.py - Phenny Logging Module
Copyright 2014, sfan5
"""

import time

loglevels = {
	'TEXT':    'TXT', # TEXT:    purely informal message that appears in masses e.g. a command being executed
	'EVENT':   'EVT', # EVENT:   like TEXT events but more likely someone wants to see those
	'ACTION':  'ACT', # ACTION:  something the bot decided on doing automatically, requires attention
	'WARNING': 'WRN', # WARNING: a warning
}

actionchannel = "##minetestbot"
actionhighlight = "sfan5"

def log(level, text, phenny):
	level = level.upper()
	f = open("bot.log", "a")
	f.write(time.strftime("%F %H:%M:%S %z") + "\t" + loglevels[level] + "\t" + text + "\n")
	f.close()
	if level == 'ACTION':
		phenny.write(['PRIVMSG', actionchannel], actionhighlight + ": " + text)
	print(level + " " + text)

def fmt_user(input):
	return "%s(%s)" % (input.nick, input.hostmask)

class SomeObject(object):
	pass

log_api = SomeObject()
log_api.log = log
log_api.fmt_user = fmt_user

_export = {
	'log': log_api,
}

def log_text(phenny, input, func):
  if func.event != "PRIVMSG": return True
  log("text", "%s executes command '%s'" % (fmt_user(input), input.group(0)), phenny)
  return True

log_text.hook = True
