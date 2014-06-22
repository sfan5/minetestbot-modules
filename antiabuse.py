#!/usr/bin/env python
"""
antiabuse.py - Phenny AntiAbuse Module
Copyright 2012, sfan5
"""
import time, sqlite3

antiabuse = {}
antiabuse["ignorelist"] = []
antiabuse["cooldown_l"] = {}
antiabuse["cooldown"] = 3 # seconds

def aa_hook(phenny, input):
    if input.admin or input.owner:
        return False

    # Ignore list
    for entry in antiabuse["ignorelist"]:
      if phenny.match_hostmask(entry, input.hostmask):
        return True # abort command

    # Cooldown
    try:
        ot = antiabuse["cooldown_l"][input.nick]
    except:
        ot = 0
    antiabuse["cooldown_l"][input.nick] = time.time()
    if antiabuse["cooldown_l"][input.nick] - antiabuse["cooldown"] < ot:
        return True # abort command
        pass

    return False

aa_hook.event = 'THISWONTHAPPEN'
aa_hook.priority = 'high'
aa_hook.rule = r'h^'
#XXX: hacky

def hmasktrans(va):
    a = "!" in va
    b = "@" in va
    if not a and not b:
        return va + "!*@*"
    elif a and not b:
        return va + "@*"
    elif not a and b:
        return "*!" + va
    else: # a and b
        return va

def ignore(phenny, input):
	if not input.admin:
		return
	arg = hmasktrans(input.group(2).strip())
	antiabuse["ignorelist"].append(arg)
	db = sqlite3.connect("antiabuse.sqlite")
	c = db.cursor()
	c.execute("INSERT INTO ignore (nick) VALUES (?)", (arg,))
	c.close()
	db.commit()
	db.close()
	phenny.reply("'%s' added to ignore list." % arg)

ignore.commands = ['ignore']
ignore.priority = 'high'

def unignore(phenny, input):
	if not input.admin:
		return
	arg = hmasktrans(input.group(2).strip())
	if not arg in antiabuse["ignorelist"]:
		return
	antiabuse['ignorelist'].remove(arg)
	db = sqlite3.connect("antiabuse.sqlite")
	c = db.cursor()
	c.execute("DELETE FROM ignore WHERE nick = ?", (arg,))
	c.close()
	db.commit()
	db.close()
	phenny.reply("'%s' removed from ignore list." % arg)

unignore.commands = ['unignore']
unignore.priority = 'high'

def listignore(phenny, input):
	if not input.admin:
		return
	phenny.reply(', '.join(antiabuse['ignorelist']))

listignore.commands = ['listignore']
listignore.priority = 'high'

db = sqlite3.connect("antiabuse.sqlite")
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS ignore (nick text)''')
c.execute("SELECT * FROM ignore")
while True:
	e = c.fetchone()
	if not e:
		break
	antiabuse["ignorelist"].append(e[0])
c.close()
db.commit()
db.close()
