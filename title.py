#!/usr/bin/env python
"""
title.py - Phenny URL Title Module
Copyright 2008, Sean B. Palmer, inamidst.com
Modified by sfan5, 2013
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import re, urllib2, urlparse

r_title = re.compile(r'(?ims)<title[^>]*>(.*?)</title\s*>')

def f_title(phenny, input): 
    uri = input.group(2)
    uri = (uri or '').encode('utf-8')

    if not uri and hasattr(phenny.bot, 'last_seen_uri'):
        uri = phenny.bot.last_seen_uri
    if not uri:
        return phenny.reply('I need a URI to give the title of...')

    if not ':' in uri:
        uri = 'http://' + uri

    try:
        redirects = 0
        while True:
            headers = {
                'Accept': 'text/html',
                'User-Agent': 'Mozilla/5.0 (MinetestBot)'
            }
            req = urllib2.Request(uri, headers=headers)
            u = urllib2.urlopen(req)
            info = u.info()
            u.close()

            if not isinstance(info, list):
                status = '200'
            else:
                status = str(info[1])
                info = info[0]
            if status.startswith('3'):
                uri = urlparse.urljoin(uri, info['Location'])
            else: break

            redirects += 1
            if redirects >= 20:
                return phenny.reply("Too many redirects")

        try: mtype = info['content-type']
        except:
            return phenny.reply("Couldn't get the Content-Type, sorry")
        if not (('/html' in mtype) or ('/xhtml' in mtype)):
            return phenny.reply("Document isn't HTML")

        u = urllib2.urlopen(req)
        bytes = u.read(262144)
        u.close()

    except IOError:
        return phenny.reply("Can't connect to %s" % uri)

    m = r_title.search(bytes)
    if m:
        title = m.group(1)
        title = title.strip()
        title = title.replace('\n', ' ')
        title = title.replace('\r', ' ')
        while '  ' in title:
            title = title.replace('  ', ' ')
        if len(title) > 100:
            title = title[:100] + '[...]'

        if title:
            try: title.decode('utf-8')
            except:
                try: title = title.decode('iso-8859-1').encode('utf-8')
                except: title = title.decode('cp1252').encode('utf-8')
            else: pass
        else: title = '[The title is empty.]'

        title = title.replace('\n', '')
        title = title.replace('\r', '')
        return phenny.reply(title)
    else: return phenny.reply('No title found')

f_title.commands = ['title']

def noteuri(phenny, input):
     uri = input.group(1).encode('utf-8')
     phenny.bot.last_seen_uri = uri

noteuri.rule = r'.*(https?://[^<> "\x01]+).*'
noteuri.priority = 'low'

if __name__ == '__main__':
    print __doc__.strip()
