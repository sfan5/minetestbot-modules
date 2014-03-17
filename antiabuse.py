#!/usr/bin/env python
"""
antiabuse.py - Phenny AntiAbuse Module
Copyright 2012, Sfan5
"""
import time, sqlite3

antiabuse = {}
antiabuse["timeout"] = {}
antiabuse["ignorelist"] = []
antiabuse["s_timeout"] = 3 # in Seconds

def aa_hook(phenny, input):
    if input.admin or input.owner:
        return False
    #Ignore-List check
    if input.nick in antiabuse["ignorelist"]:
        return True # abort command
    #Timeout check
    try:
        ot = antiabuse["timeout"][input.nick]
    except:
        ot = 0
    antiabuse["timeout"][input.nick] = time.time()
    if antiabuse["timeout"][input.nick] - antiabuse["s_timeout"] < ot:
        return True # abort command
        pass
    
    return False
aa_hook.event = 'THISWONTHAPPEN'
aa_hook.priority = 'high'
aa_hook.rule = r'h^'
#Warning: Uses a very very dirty hack to achieve that other modules can access this function

def ignore(phenny, input):
	if not input.admin:
		return
	arg = input.group(2).strip()
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
	arg = input.group(2).strip()
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


