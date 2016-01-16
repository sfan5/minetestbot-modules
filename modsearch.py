#!/usr/bin/env python
"""
modsearch.py - Phenny Minetest Mod Search Module
Copyright 2015-2016, SmallJoker
Licensed under GNU General Public License v2.0
"""

import web

def mod(phenny, input):
	uri = "http://krock-works.16mb.com/MTstuff/modSearchAPI.php?q="
	text, sc = web.get(uri + web.urlencode(input.group(2)))
	text = str(text, 'utf-8')
	data = web.json(text)
	answer = ""
	if "error" in data:
		answer = data["error"]
	else:
		answer = (data["title"] + 
			" by " + data["author"] +
			" - " + data["link"])

	phenny.reply(answer)

mod.commands = ['mod']
mod.example = '.mod party_mod'

if __name__ == '__main__':
	print(__doc__)
