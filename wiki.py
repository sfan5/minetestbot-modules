#!/usr/bin/env python
"""
wiki.py - Phenny Wiki Module
Copyright 2014, sfan5
Licensed under GNU General Public License v2.0
"""

import re
import web
import urllib.parse

wikiuri_g = 'http://wiki.minetest.net/index.php?title=%s&printable=yes'
wikiuri_r = 'http://wiki.minetest.net/%s'

r_content = re.compile(r'(?i)<div[^>]+class=.mw-content-ltr.>')
r_paragraph = re.compile(r'(?ims)<p>(.+?)</p>')
r_headline = re.compile(r'(?i)<span class="mw-headline" id="[^"]+">(.+?)</span>')
r_sentenceend = re.compile(r'\.[ A-Z]')
transforms = [
	(re.compile(r'(?i)<a [^>]+>(.+?)</a>'), "\x0302\g<1>\x0f"),
	(re.compile(r'(?i)<b>(.+?)</b>'), "\x02\g<1>\x02"),
	(re.compile(r'(?i)<i>(.+?)</i>'), "\x1d\g<1>\x1d"),
	(re.compile(r'(?i)<u>(.+?)</u>'), "\x1f\g<1>\x1f"),
	(re.compile(r'(?i)<code>(.+?)</code>'), "\x0315\g<1>\x0f"),
	(re.compile(r'(?i)<br\s*/?>'), ""),
]
nottext = [
	re.compile(r'(?i)^<br\s*/?>$'),
	re.compile('(?i)^' + re.escape('<b>This article is incomplete.</b>') + '$'),
	re.compile('(?i)^' + re.escape('Please help expand this article to include more useful information.') + '$'),
]

def wiki(phenny, input):
	term = input.group(2)
	if not term:
		return

	log.log("event", "%s queried Wiki for '%s'" % (log.fmt_user(input), term), phenny)
	term = term.replace(" ", "_")
	term = web.urlencode(term)

	data, scode = web.get(wikiuri_g % term)
	if scode == 404:
		return phenny.say("No such page.")
	data = str(data, "utf-8")

	m = re.search(r_content, data)
	if not m:
		return phenny.say("Sorry, did not find any text to display. Here's the link: %s" % (wikiuri_r % term,))
	data = data[m.span()[1]:]

	mi = re.finditer(r_paragraph, data)
	text = ""
	for m in mi:
		abort = False
		for e in nottext:
			if re.search(e, m.group(1)):
				abort = True
				break
		if abort:
			continue
		text = m.group(1)
		break
	if not text:
		m = re.search(r_headline, data)
		if m:
			text = "<b>" + m.group(1) + "</b>"
		else:
			return phenny.say("Sorry, did not find any text to display. Here's the link: %s" % (wikiuri_r % term,))
	for tf in transforms:
		text = re.sub(tf[0], tf[1], text)
	m = re.search(r_sentenceend, text)
	if m:
		text = text[:m.span()[1]-1]
	phenny.say('"%s" - %s' % (web.decode(text), wikiuri_r % term))

wiki.commands = ['wik', 'wiki']
wiki.priority = 'high'

if __name__ == '__main__':
	print(__doc__.strip())
