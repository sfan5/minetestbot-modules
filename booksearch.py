#!/usr/bin/env python
"""
booksearch.py - Phenny Minetest Modding Book Search Module
Copyright 2018, rubenwardy
Licensed under GNU General Public License v2.0
"""

import web

def book(phenny, input):
	uri = "https://rubenwardy.com/minetest_modding_book/sitemap.json"
	text, sc = web.get(uri)
	text = str(text, 'utf-8')
	data = web.json(text)

	query = input.group(2).lower()
	for ele in data:
		title = ele["title"]
		desc  = ele.get("description")
		if query in title.lower() or (desc is not None and query in desc.lower()):
			phenny.reply(title + " - " + ele["loc"])
			return

	phenny.reply("Unable to find " + input.group(2))

book.commands = ['book']
book.example = '.book folder structure'

if __name__ == '__main__':
	print(__doc__)
