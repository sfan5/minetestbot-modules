#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2013, sfan5
"""

import random
import sqlite3
import time
import calendar
import hashlib

tell_list = []
tell_pending = []

def tell_diskwr():
	global tell_pending, tell_list
	db = sqlite3.connect("tell.sqlite")
	c = db.cursor()
	for tr in tell_pending:
		if tr[0] == "del":
			r = c.execute("DELETE FROM tell WHERE id = ?", (tr[1], )).rowcount
			if r != 1:
				log.log("warning", "[tell] could not remove entry id %d from db?!?" % (tr[1], ))
			else:
				log.log("event", "[tell] removed entry id %d from db" % (tr[1], ))
		elif tr[0] == "add":
			c.execute("INSERT INTO tell (nick, tellee, msg, time) VALUES (?,?,?,?)", tr[1])
			tell_list.append((c.lastrowid, ) + tr[1]) # We actually insert the entry into the list here
			log.log("event", "[tell] added entry %r to db, id=%d" % (tr[1], c.lastrowid))
		else:
			log.log("warning", "[tell] unknown action type %s" % (tr[0], ))
	c.close()
	db.commit()
	db.close()
	tell_pending = []

def api_tell(teller, tellee, text):
	d = (teller, tellee, text, int(calendar.timegm(time.gmtime())))
	tell_pending.append(("add", d))
	# We do not insert the entry into tell_list yet because we don't know which id it will have
	tell_diskwr() # Write the change to disk

class SomeObject(object):
	pass

tell_api = SomeObject()
tell_api.tell = api_tell

_export = {
	'tell': tell_api,
}

def tell(phenny, input):
	arg = input.group(2)
	if not arg:
		return phenny.reply("Need a nickname...")
	if not ' ' in arg:
		return phenny.reply("...and text")
	teller = input.nick
	target = arg.split(" ")[0]
	text = " ".join(arg.split(" ")[1:])
	if target.lower() == teller.lower():
		return phenny.say("You can tell that to yourself")
	if target.lower() == phenny.nick.lower():
		return phenny.say("I'm not dumb, you know?")
	elif target[-1] == ":":
		return phenny.reply("Do not put an : at the end of nickname")

	api_tell(teller, target, text)

	response = "I'll pass that on when %s is around" % target
	rand = random.random()
	if rand > 0.85: response = "yeah, sure, whatever"
	elif rand > 0.75: response = "yeah, yeah"

	phenny.reply(response)

tell.commands = ["tell"]

def checktell(phenny, input):
	for e in tell_list:
		if e[2].lower() == input.nick.lower():
			phenny.say("%s: %s <%s> %s" % (
				input.nick,
				time.strftime('%m-%d %H:%M UTC',
					time.gmtime(e[4])),
				e[1],
				e[3]))
			try:
				tell_list.remove(e)
			except:
				log("warning", "[tell] could not remove entry %r from list?!?" % (e, ), phenny)
			tell_pending.append(("del", e[0]))
			tell_diskwr() # Write the change to disk
			break

def note(phenny, input):
	if input.sender.startswith('#'):
		checktell(phenny, input)

note.rule = r'.*'
note.priority = 'low'
note.nohook = True

def note_join(phenny, input):
	if input.sender.startswith('#'):
		checktell(phenny, input)

note_join.rule = r'.*'
note_join.event = 'JOIN'
note_join.priority = 'low'
note_join.nohook = True

db = sqlite3.connect("tell.sqlite")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tell (id INTEGER PRIMARY KEY, nick TEXT, tellee TEXT, msg TEXT, time INTEGER)")
c.execute("SELECT * FROM tell")
while True:
	e = c.fetchone()
	if not e:
		break
	tell_list.append(e)
c.close()
db.commit()
db.close()

if __name__ == '__main__':
   print(__doc__.strip())
