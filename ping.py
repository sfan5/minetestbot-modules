#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

import random

def hello(phenny, input):
   greeting = random.choice(('Hi', 'Hey', 'Hello', 'sup'))
   punctuation = random.choice(('', '!', '.'))
   phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey) $nickname[ \t]*$'

def interjection(phenny, input):
   phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'

def l3(phenny, input):
   phenny.say('<3 ' + input.nick)
l3.rule = r'<3 $nickname'
l3.priority = 'low'

if __name__ == '__main__':
   print __doc__.strip()
