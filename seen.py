#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Modified by sfan5 2013
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
from tools import deprecated
import sqlite3

def opendb():
    db = sqlite3.connect("seen.sqlite")
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS seen (nick text, channel text, time int)''')
    c.close()
    return db

def seen(phenny, input): 
    """.seen <nick> - Reports when <nick> was last seen."""
    for x in phenny.bot.commands["high"].values():
        if x[0].__name__ == "aa_hook":
            if x[0](phenny, input):
                return # Abort function
    nick = input.group(2)
    if not nick:
        return phenny.reply("Need a nickname to search for...")
    nick = nick.lower()

    print("[LOG]: %s queried Seen Result for %s" % (input.nick,nick))

    db = opendb()
    c = db.cursor()
    c.execute("SELECT channel, time FROM seen WHERE nick = ?", (nick,))
    r = c.fetchone()
    c.close()
    db.close()
    if r:
        channel, t = r[0], r[1]
        t = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(t))

        msg = "%s was last seen at %s on %s" % (nick, t, channel)
        phenny.reply(msg)
    else:
        phenny.reply("Sorry, I haven't seen %s around." % nick)

seen.rule = (['seen'], r'(\S+)')

def note(phenny, input):
    db = opendb()
    if input.sender.startswith('#'):
        c = db.cursor()
        c.execute("SELECT * FROM seen WHERE nick = ?", (input.nick.lower(),))
        if c.fetchone() != None:
            d = (input.sender, int(time.time()), input.nick.lower())
            c.execute('UPDATE seen SET channel = ?, time = ? WHERE nick = ?', d)
        else:
            d = (input.nick.lower(), input.sender, int(time.time()))
            c.execute('INSERT INTO seen VALUES (?,?,?)', d)
        db.commit()
        c.close()
    db.close()

note.rule = r'.*'
note.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
