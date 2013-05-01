#!/usr/bin/env python
"""
shorten.py - URL Shorten Module
Copyright 2013, sfan5
"""
import urllib

def shorten(phenny, input):
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    arg = input.group(2)
    if not arg:
        arg = "" # Function continues and prints Help Message
    arg = arg.split(' ')
    if len(arg) < 2:
        phenny.reply("Give me an url shorten service and an address")
        return phenny.reply("Supported Services: is.gd, v.gd")
    else:
        if arg[0].lower() == "is.gd":
            p = urllib.urlencode({'format' :"simple", 'url': arg[1]})
            try:
                u = urllib.urlopen("http://is.gd/create.php?%s" % p)
                return phenny.reply(u.read())
            except:
                return phenny.reply("Problems accessing is.gd, please try a different Service")
        if arg[0].lower() == "v.gd":
            p = urllib.urlencode({'format' :"simple", 'url': arg[1]})
            try:
                u = urllib.urlopen("http://v.gd/create.php?%s" % p)
                return phenny.reply(u.read())
            except:
                return phenny.reply("Problems accessing v.gd, please try a different Service")
        return phenny.reply("Unknown Service")
            

shorten.commands = ['shorten','sh']
shorten.thread = True

if __name__ == '__main__':
    print __doc__
