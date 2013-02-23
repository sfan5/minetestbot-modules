#!/usr/bin/env python
"""
ai.py - Phenny AutomatedResponse Module
Copyright 2013, Sfan5
"""
import random, time
ar = {}

ar["enable"] = True
ar["bn"] = "minetestbot" #lowercase bot name

def arctl(phenny, input):
    if not input.admin or not input.owner: return
    arg = input.group(2)
    if not arg:
        return
    if arg == "enable":
        ar["enable"] = True
        phenny.say("AR enabled.")
    elif arg == "disable":
        ar["enable"] = False
        phenny.say("AR disabled.")

arctl.commands = ['ar']
aictl.priority = 'low'

def response(personal, nick, msg):
    if personal:
        return msg
    else:
        return nick + ": " + msg

def arp(phenny, input):
    if not ar["enable"]:
        return
    ar["lm"] = [input.nick, input.bytes.strip(), time.time()]
    for x in phenny.bot.commands["high"].values():
       if x[0].__name__ == "aa_hook":
           if x[0](phenny, input):
               return # Abort function
    sia = input.bytes.strip().strip('?!').lower().split(" ")
    #print(sia)
    si = sia.__iter__()
    try:
        sn = si.next()
        personal = not input.sender.startswith("#")
        if sn.startswith("minetestbot"):
            sn = si.next()
            personal = True
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
                if si.next().startswith(ar["bn"]) or personal:
                    return phenny.say(response(personal, input.nick, "Although i'm only a bot I appreciate your thanks."))
        if sn == "thanks":
            if si.next().startswith(ar["bn"]) or personal:
                return phenny.say(response(personal, input.nick, "Although i'm only a bot I appreciate your thanks."))
        if sn == "back":
            return phenny.say("Welcome back " + input.nick + "!")
        if sn == "should":
            sn = si.next()
            if sn == "i":
                sn = si.next()
                if sn == "eat" or sn == "drink":
                    sn = si.next()
                    if sn == "a" or sn == "an" or sn == "the": sn = si.next()
                    if sn == "kitty" or sn.startswith("kitte") or sn.startswith("cat"):
                        return phenny.reply("I don't recommend eating kittens")
                    elif sn == "air":
                        return phenny.reply("Eating air won't hurt you")
                    elif sn == "bot" or sn == ar["bn"] or (sn == "you" and personal):
                        return phenny.reply("Don't eat me D:")
                    elif sn == "acid":
                        return phenny.say(response(personal, input.nick, "Don't!!"))
                    else:
                        return phenny.reply("You decide")
        if sn == "\x01action":
            sn = si.next()
            if sn == "hugs":
                sn = si.next()
                if sn != ar["bn"] and random.randint(0,3) == 0:
                    return phenny.say("Can I get a hug too? Please")
                else:
                    return phenny.reply(" :D")
            if sn == "puts":
                sn = si.next()
                if sn == "a" or sn == "an" or sn == "the": sn = si.next()
                r = sn
                sn = si.next()
                if sn == "on" or sn == "under" or sn == "behind" or sn == "in" or sn == "above":
                    sn = si.next()
                    if sn.startswith(ar["bn"]):
                        if r.startswith("kitt") or r.startswith("cat"):
                            return phenny.reply("I don't want it, talk to NekoGloop, he likes kittens")
                        elif r.startswith("pupp") or r.startswith("dog"):
                            return phenny.reply("Awwwww....")
                        elif r.startswith("bomb") or r.startswith("explosive") or r.startswith("dynamite"):
                            if random.randint(0,3) == 0:
                                return phenny.say("*shoots " + input.nick + " with an AK-74*")
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
                        return phenny.say(response(personal, input.nick, "There is a detailed guide at https://raw.github.com/celeron55/minetest/master/README.txt for compiling minetest on windows and linux, if you have a mac.. ..no luck"))
                if sn == "install":
                    sn = si.next()
                    if sn == "a" or sn == "an": sn = si.next()
                    if sn.startswith("mod"):
                        return phenny.say(response(personal, input.nick, "You can usually find installation instruction in the mod topic, http://wiki.minetest.com/wiki/Mods also describes how to install mods"))
                    if sn == "texture":
                        if si.next().startswith("pack"):
                            return phenny.say(response(personal, input.nick, "http://wiki.minetest.com/wiki/Texture_Packs provides a good guide on how to install texture packs"))
                if sn == "craft":
                    sn = si.next()
                    if sn == "a" or sn == "an" or sn.endswith("s"):
                        return phenny.say(response(personal, input.nick, "Take a look at http://wiki.minetest.com/wiki/Crafting ,you should find it there"))
        if sn == "where":
            sn = si.next()
            r = (False, 0)
            if sn == "are" or sn == "is":
                r = (True, 0)
            if sn == "do" or sn == "did":
                r = (True, 1)
            if r[0]:
                sn = si.next()
                if (sn == "you" and personal) or (sn == ar["bn"] and not personal):
                    sn = si.next()
                    if sn == "come" and r[1] == 1: sn = si.next()
                    if sn == "from":
                        if random.randint(0,5) == 0:
                            return phenny.say(response(personal, input.nick, "I'm from the Bot Universe and i'm going to destroy you... BEEP BOOP BLEEP BOOP"))
                        else:
                            return phenny.say(response(personal, input.nick, "I come from https://github.com/sfan5/minetestbot-modules"))
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
                        return phenny.say(response(personal, input.nick, "http://www.minetest.net/download.php  Please note that it is recommend to compile Minetest yourself if you use GNU/Linux"))
                    if sn.startswith("mod"):
                        return phenny.say(response(personal, input.nick, "http://forum.minetest.net/viewforum.php?id=11"))
                    if sn.startswith("texture"):
                        if si.next().startswith("pack"):
                            return phenny.say(response(personal, input.nick, "http://forum.minetest.net/viewforum.php?id=4"))
                    if sn.startswith("server") and r[1] == 1:
                        return phenny.say(response(personal, input.nick, "http://forum.minetest.net/viewforum.php?id=10 and http://servers.minetest.ru"))
                    elif sn.startswith("server") and r[1] == 0:
                        return phenny.say(response(personal, input.nick, "Download Minetest at http://www.minetest.net/download.php and run 'minetest.exe --server' to start a server instance"))
                    if sn.startswith("map"):
                        return phenny.say(response(personal, input.nick, "http://forum.minetest.net/viewforum.php?id=12"))
    except:
        return

arp.priority = 'medium'
arp.rule = r'.*'
arp.event = '*'

if __name__ == '__main__': 
    print __doc__.strip()
