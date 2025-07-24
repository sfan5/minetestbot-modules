#!/usr/bin/env python
"""
contentdb.py - Phenny ContentDB Search Module
Copyright 2025, sfan5
Licensed under GNU General Public License v2.0
"""

import web
import re
import time
import random

BASEURL = "https://content.luanti.org/"

cached_data = None
def get_cdb():
	global cached_data
	if not cached_data or cached_data[0] < time.time() - 30*60:
		uri = BASEURL + "api/packages/?type=mod&type=game&type=txp&hide=desktop_default"
		text, sc = web.get(uri)
		cached_data = ( time.time(), web.json(text.decode('utf-8')) )
	return cached_data[1]

def soup(s):
	s = re.sub("\s+", " ", s)
	s = re.sub(r"[^\w ]+", "", s) # leave only words
	return set(s.lower() for s in s.split(" ") if s)

def find_match(data, search):
	# exact match
	for mod in data:
		if search in (mod["name"].lower(), mod["title"].lower()):
			return mod
	# word-based best match
	can = []
	s1 = soup(search)
	for mod in data:
		s2 = soup(mod["title"])
		if len(s1.intersection(s2)) > 0:
			score = 10 * len(s1.intersection(s2)) - len(s2.difference(s1))
			can.append((score, mod))
	if can:
		return sorted(can, key=lambda x: x[0], reverse=True)[0][1]
	# prefix match
	if len(search) > 2:
		for mod in data:
			if mod["name"].lower().startswith(search) or mod["title"].lower().startswith(search):
				return mod
	return None

types = {
	"txp": "Texture Pack",
	"mod": "Mod",
	"game": "Game",
}

def mod(phenny, input):
	data = get_cdb()
	assert isinstance(data, list)
	if input.group(2):
		mod = find_match(data, input.group(2))
	else:
		mod = random.choice(data)

	if not mod:
		return phenny.reply("Nothing found.")
	pkgurl = BASEURL + "packages/" + web.urlencode(mod["author"]) + "/" + web.urlencode(mod["name"]) + "/"
	answer = (
		types[mod["type"]] + ": " +
		mod["title"] + " [" + mod["name"] + "]" +
		" by " + mod["author"] +
		" - " + pkgurl
	)
	phenny.reply(answer)

mod.commands = ['mod', 'cdb']
mod.example = '.mod block users'

if __name__ == '__main__':
	print(__doc__)
