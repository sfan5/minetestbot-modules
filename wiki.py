#!/usr/bin/env python
"""
wiki.py - Phenny Wiki Module
Copyright 2014, sfan5
"""

import re
import web
import urllib.parse

wikiuri_g = 'http://wiki.minetest.net/%s?printable=yes'
wikiuri_r = 'http://wiki.minetest.net/%s'

r_content = re.compile(r'(?i)<div[^>]+class=.mw-content-ltr.>')
r_paragraph = re.compile(r'(?ims)<p>(.+?)</p>')
r_sentenceend = re.compile(r'\.[^\.]')
transforms = [
	re.compile(r'(?i)<a [^>]+>(.+?)</a>'),
	re.compile(r'(?i)<b>(.+?)</b>'),
	re.compile(r'(?i)<i>(.+?)</i>'),
]

def wiki(phenny, input):
	term = input.group(2)
	if not term:
		return

	log.log("event", "%s queried Wiki for '%s'" % (log.fmt_user(input), term), phenny)
	term = web.urlencode(term)

	data, scode = web.get(wikiuri_g % term)
	if scode == 404:
		return phenny.say("No such page.")
	data = str(data, "utf-8")

	m = re.search(r_content, data)
	if not m:
		return phenny.say("Sorry, did not find anything.")
	data = data[m.span()[1]:]

	m = re.search(r_paragraph, data)
	if not m:
		return phenny.say("Sorry, did not find anything.")
	data = m.group(1)
	for transform in transforms:
		data = re.sub(transform, '\g<1>', data)
	m = re.search(r_sentenceend, data)
	if m:
		data = data[:m.span()[1]-1]
	phenny.say('"%s" - %s ' % (web.decode(data), wikiuri_r % term))

wiki.commands = ['wik', 'wiki']
wiki.priority = 'high'

if __name__ == '__main__':
	print(__doc__.strip())
