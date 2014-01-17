#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2013, sfan5
"""

import random
from tools import deprecated
from thread import start_new_thread, allocate_lock
import sqlite3

tell_list = []
telldb_lock = allocate_lock()

def tell(phenny, input): 
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return # Abort function
	arg = input.group(2)
	if not arg:
		return phenny.reply("Need a nickname...")
	if not ' ' in arg:
		return phenny.reply("...and text")
	teller = input.nick
	target = arg.split(" ")[0]
	text = " ".join(arg.split(" ")[1:])
	d = (teller, target, text)
	if target.lower() == teller.lower():
		return phenny.say("You can tell that to yourself")
	if target.lower() == phenny.nick.lower():
		return phenny.say("I'm not dumb, you know?")

	telldb_lock.acquire()
	tell_list.append(d)
	db = sqlite3.connect("tell.sqlite")
	c = db.cursor()
	c.execute("INSERT INTO tell VALUES (?,?,?)", d)
	c.close()
	db.commit()
	db.close()
	telldb_lock.release()

	response = "I'll pass that on when %s is around" % target
	rand = random.random()
	if rand > 0.99: response = "yeah, yeah"
	elif rand > 0.9: response = "yeah, sure, whatever"

	phenny.reply(response)

tell.commands = ["tell"]

def checktell(phenny, input):
	for e in tell_list:
		if e[1].lower() == input.nick.lower():
			phenny.say("%s: <%s> %s" % (input.nick, e[0], e[2]))
			telldb_lock.acquire()
			tell_list.remove(e)
			db = sqlite3.connect("tell.sqlite")
			c = db.cursor()
			c.execute("DELETE FROM tell WHERE nick = ? AND channel = ? AND msg = ?", e)
			c.close()
			db.commit()
			db.close()
			telldb_lock.release()
			return

def note(phenny, input):
	if input.sender.startswith('#'):
		checktell(phenny, input)

note.rule = r'.*'
note.priority = 'low'

def note_join(phenny, input):
	if input.sender.startswith('#'):
		checktell(phenny, input)

note_join.rule = r'.*'
note_join.event = 'JOIN'
note_join.priority = 'low'

#telldb_lock.acquire() # Just to be safe
db = sqlite3.connect("tell.sqlite")
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tell (nick text, channel text, msg text)")
c.execute("SELECT nick, channel, msg FROM tell")
while True:
	e = c.fetchone()
	if not e:
		break
	tell_list.append(e)
c.close()
db.close()
#telldb_lock.acquire()

if __name__ == '__main__': 
   print __doc__.strip()
