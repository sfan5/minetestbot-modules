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

def api_ignore(mask):
  antiabuse["ignorelist"].append(mask)
  db = sqlite3.connect("antiabuse.sqlite")
  c = db.cursor()
  c.execute("INSERT INTO ignore (nick) VALUES (?)", (mask,))
  c.close()
  db.commit()
  db.close()

def api_unignore(mask):
  if not mask in antiabuse["ignorelist"]:
    return False
  antiabuse['ignorelist'].remove(mask)
  db = sqlite3.connect("antiabuse.sqlite")
  c = db.cursor()
  c.execute("DELETE FROM ignore WHERE nick = ?", (mask,))
  c.close()
  db.commit()
  db.close()
  return True

def api_get_ignorelist():
  return antiabuse["ignorelist"]

class SomeObject(object):
  pass

antiabuse_api = SomeObject()
antiabuse_api.ignore = api_ignore
antiabuse_api.unignore = api_unignore
antiabuse_api.get_ignorelist = api_get_ignorelist

_export = {
  'antiabuse': antiabuse_api,
}

def aa_hook(phenny, input, func):
    if input.admin or input.owner:
        return True

    # Ignore list
    for entry in antiabuse["ignorelist"]:
      if phenny.match_hostmask(entry, input.hostmask):
        return False # abort command

    # Cooldown
    if input.nick in antiabuse["cooldown_l"]:
        ot = antiabuse["cooldown_l"][input.nick]
    else:
        ot = 0
    antiabuse["cooldown_l"][input.nick] = time.time()
    if antiabuse["cooldown_l"][input.nick] - antiabuse["cooldown"] < ot:
        return False # abort command
        pass

    return True

aa_hook.hook = True

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
	r = api_ignore(arg)
	if r:
		phenny.reply("'%s' added to ignore list." % arg)
	else:
		phenny.reply("'%s' not in ignore list." % arg)

ignore.commands = ['ignore']
ignore.priority = 'high'

def unignore(phenny, input):
	if not input.admin:
		return
	arg = hmasktrans(input.group(2).strip())
	api_unignore(arg)
	phenny.reply("'%s' removed from ignore list." % arg)

unignore.commands = ['unignore']
unignore.priority = 'high'

def limjoin(ent, j, lim):
	o = []
	i = 0
	while True:
		if i == len(ent):
			break
		s = ""
		while True:
			if i == len(ent) or len(s) + len(ent[i]) > lim:
				break
			s += ent[i]
			i += 1
			s += j
		o.append(s)
	if len(o) > 0:
		for i in range(len(o)):
			o[i] = o[i][:-len(j)] # Cut off the delimiter
	return o
		

def listignore(phenny, input):
	if not input.admin:
		return
	if len(antiabuse['ignorelist']) == 0:
		return phenny.reply("Ignore list empty.")
	l = limjoin(antiabuse['ignorelist'], ', ', 400)
	for s in l:
		phenny.reply(s)

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
