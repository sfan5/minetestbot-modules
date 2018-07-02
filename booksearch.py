#!/usr/bin/env python
"""
booksearch.py - Phenny Minetest Modding Book Search Module
Copyright 2018, rubenwardy
Licensed under GNU General Public License v2.0
"""

import web

def book(phenny, input):
	uri = "https://rubenwardy.com/minetest_modding_book/sitemap.json"
	text, status = web.get(uri)
	text = str(text, 'utf-8')
	data = web.json(text)

	query = (input.group(2) or "").lower().strip()
	if not query:
		phenny.reply("Minetest Modding Book - https://rubenwardy.com/minetest_modding_book/")
		return
	
	for ele in data:
		title = ele["title"]
		desc  = ele.get("description", "")
		if query in title.lower() or query in desc.lower():
			return phenny.reply(title + " - " + ele["loc"])

	phenny.reply("Nothing found.")

book.commands = ['book']
book.example = '.book folder structure'

if __name__ == '__main__':
	print(__doc__)
