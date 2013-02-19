#!/usr/bin/env python
"""
ai.py - Phenny AI Module (EXPERIMENTAL)
Copyright 2013, Sfan5
"""
import random
ai = {}

ai["enable"] = False
ai["bn"] = "minetestbot" #lowercase bot name

def aictl(phenny, input):
    if not input.admin or not input.owner: return
    arg = input.group(2)
    if not arg:
        return
    if arg == "enable":
        ai["enable"] = True
        phenny.say("AI enabled.")
    elif arg == "disable":
        ai["enable"] = False
        phenny.say("AI disabled.")

aictl.commands = ['ai']
aictl.priority = 'low'

def aip(phenny, input):
    if not ai["enable"]:
        return
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    sia = input.bytes.strip().strip('?!').lower().split(" ")
    #print(sia)
    si = sia.__iter__()
    try:
        sn = si.next()
        if sn.startswith("minetestbot"): sn = si.next()
        if sn == "hi" or sn == "hey" or sn == "hello":
            try:
                sn = si.next()
            except StopIteration:                        
                return phenny.say("hi " + input.nick)
            if sn == "guys" or sn == "folks" or sn == "people" or sn.startswith("every") or sn == "all":
                return phenny.say("hi " + input.nick)
        if sn == "o.o":
            return phenny.reply("What are you wondering about?")
        if sn == "thank":
            if si.next() == "you":
                if si.next().startswith(ai["bn"]):
                    return phenny.reply("Although i'm only a bot I appreciate your thanks.")
        if sn == "thanks":
            if si.next().startswith(ai["bn"]):
                return phenny.reply("Although i'm only a bot I appreciate your thanks.")
        if sn == "back":
            return phenny.reply("Welcome back!")
        if sn == "should":
            sn == si.next()
            if sn == "i":
                sn = si.next()
                if sn == "eat" or sn == "drink":
                    sn = si.next()
                    if sn == "a" or sn == "an" or sn == "the": sn = si.next()
                    if sn == "kitty" or sn.startswith("kitten") or sn.startswith("cat"):
                        return phenny.reply("I don't recommend eating kittens")
                    elif sn == "air":
                        return phenny.reply("Eating air won't hurt you")
                    elif sn == "bot" or sn == ai["bn"] or sn == "you":
                        return phenny.reply("Don't eat me D:")
                    else:
                        return phenny.reply("If it's acid, no, otherwise yes")
        if sn == "\x01action":
            sn = si.next()
            if sn == "hugs":
                sn = si.next()
                if sn != ai["bn"] and random.randint(0,3) == 0:
                    return phenny.say("Can I get a hug too? Please")
                else:
                    return phenny.reply(" :D")
            if sn == "puts":
                sn = si.next()
                if sn == "a" or sn == "an" or sn == "the": sn = si.next()
                r = sn
                sn = si.next()
                if sn == "on" or sn == "under" or sn == "behind":
                    sn = si.next()
                    if sn.startswith(ai["bn"]):
                        if r.startswith("kitt") or r.startswith("cat"):
                            return phenny.reply("I don't want it, talk to NekoGloop, he likes kittens")
                        elif r.startswith("bomb") or r.startswith("explosive") or r.startswith("dynamite"):
                            return phenny.say("*runs away*")
                        elif r.startswith("cookie") or r.startswith("cake"):
                            return phenny.say("Ooh! thank you, nom nom nom...")
        if sn == "how":
            sn = si.next()
            r = False
            if sn == "to":
                r = True
            if sn == "do" or sn == "can":
                sn = si.next()
                if sn == "i" or sn == "you":
                    r = True
            if r:
                sn = si.next()
                if sn == "compile":
                    sn = si.next()
                    if sn == "minetest":
                        return phenny.reply("There is a detailed guide at https://raw.github.com/celeron55/minetest/master/README.txt for compiling minetest on windows and linux, if you have a mac.. ..no luck")
                if sn == "install":
                    sn = si.next()
                    if sn == "a" or sn == "an": sn = si.next()
                    if sn.startswith("mod"):
                        return phenny.reply("You can usually find installation instruction in the mod topic, http://wiki.minetest.com/wiki/Mods also describes how to install mods")
                    if sn == "texture":
                        if si.next().startswith("pack"):
                            return phenny.reply("http://wiki.minetest.com/wiki/Texture_Packs provides a good guide on how to install texture packs")
                if sn == "craft":
                    sn = si.next()
                    if sn == "a" or sn == "an" or sn.endswith("s"):
                        return phenny.reply("Take a look at http://wiki.minetest.com/wiki/Crafting ,you should find it there")
        if sn == "where":
            sn = si.next()
            if sn == "can" or sn == "could" or sn == "to":
                sn = si.next()
                if sn == "i": sn = si.next()
                r = (False, 0)
                if sn == "get" or sn == "download":
                    r = (True, 0)
                if sn == "find":
                    r = (True, 1)
                if r[0]:
                    sn = si.next()
                    if sn == "a" or sn == "an" or sn == "the": sn = si.next()
                    try:
                        sn = si.next()
                    except StopIteration:                        
                        return phenny.reply("http://www.minetest.net/download.php  Please note that it is recommend to compile Minetest yourself if you use GNU/Linux")
                    if sn.startswith("mod"):
                        return phenny.reply("http://forum.minetest.net/viewforum.php?id=11")
                    if sn.startswith("texture"):
                        if si.next().startswith("pack"):
                            return phenny.reply("http://forum.minetest.net/viewforum.php?id=4")
                    if sn.startswith("server") and r[1] == 1:
                        return phenny.reply("http://forum.minetest.net/viewforum.php?id=10 and http://servers.minetest.ru")
                    elif sn.startswith("server") and r[1] == 0:
                        return phenny.reply("Download Minetest at http://www.minetest.net/download.php and run 'minetest.exe --server' to start a server instance")
                    if sn.startswith("map"):
                        return phenny.reply("http://forum.minetest.net/viewforum.php?id=12")
    except:
        return

aip.priority = 'medium'
aip.rule = r'.*'
aip.event = '*'

if __name__ == '__main__': 
    print __doc__.strip()
