#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2017 sfan5
Licensed under GNU General Public License v2.0
"""

import os.path
import time
from threading import Thread, Lock
import sqlite3

DBPATH = "seen.sqlite"
updates = list()
updates_l = Lock()

def updatethread():
	global updates, updates_l
	db = sqlite3.connect(DBPATH)
	while True:
		if len(updates) == 0:
			time.sleep(15)
			continue
		updates_l.acquire()
		up = updates
		updates = list()
		updates_l.release()

		db.executemany("REPLACE INTO seen(channel, time, nick) VALUES (?, ?, ?)", up)
		db.commit()
	db.close()

def pushupdate(sender, nick):
	ts = int(time.mktime(time.gmtime()))
	nick = nick.lower()

	updates_l.acquire()
	updates.append((sender, ts, nick))
	updates_l.release()


class SeenApi(object):
	@staticmethod
	def seen(nick):
		db = sqlite3.connect(DBPATH)
		c = db.execute("SELECT channel, time FROM seen WHERE nick = ?", (nick, ))
		r = c.fetchone()
		db.close()
		return r

_export = {
	'seen': SeenApi,
}


def seen(phenny, input):
	"""seen <nick> - Reports when <nick> was last seen."""
	nick = input.group(2)
	if not nick:
		return phenny.reply("Need a nickname to search for...")
	nick = nick.lower()

	log.log("event", "%s queried Seen database for '%s'" % (log.fmt_user(input), nick), phenny)

	r = SeenApi.seen(nick)
	if r is None:
		return phenny.reply("Sorry, I haven't seen %s around." % nick)

	channel, t = r[0], r[1]
	t = time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(t))
	phenny.reply("%s was last seen at %s on %s" % (nick, t, channel))

seen.rule = (['seen'], r'(\S+)')


def create_note(event=None):
	def f(phenny, input):
		if input.sender.startswith("#"):
			pushupdate(input.sender, input.nick)
	f.rule = r'.*'
	f.priority = "low"
	f.thread = False
	f.nohook = True
	if event is not None:
		f.event = event
	return f

note = create_note()
note_join = create_note("JOIN")
note_part = create_note("PART")


if not os.path.exists(DBPATH):
	db = sqlite3.connect(DBPATH)
	db.execute('''
	CREATE TABLE `seen` (
		`nick` tinytext NOT NULL,
		`channel` tinytext NOT NULL,
		`time` int NOT NULL,
		PRIMARY KEY (`nick`)
	)
	''')
	db.close()

t = Thread(target=updatethread, name="seen.py database thread")
t.start()


if __name__ == '__main__':
	print(__doc__.strip())
