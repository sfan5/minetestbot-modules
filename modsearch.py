#!/usr/bin/env python
"""
modsearch.py - Phenny Minetest Mod Search Module
Copyright 2015-2016, SmallJoker
Licensed under GNU General Public License v2.0
"""

import web

def mod(phenny, input):
	uri = "https://krock-works.nex.sh/minetest/modSearchAPI.php?q="
	text, sc = web.get(uri + web.urlencode(input.group(2) or ""))
	text = str(text, 'utf-8')
	data = web.json(text)
	answer = ""
	if "error" in data:
		answer = data["error"]
	else:
		answer = (data["title"] +
			" by " + data["author"] +
			" - " + data["link"])
		if "source" in data:
			answer += " - " + data["source"]

	phenny.reply(answer)

mod.commands = ['mod']
mod.example = '.mod party_mod'

if __name__ == '__main__':
	print(__doc__)
