#!/usr/bin/env python
"""
forumutils.py - Phenny Minetest Forum Module
Copyright 2012, sfan5
"""

import web
from xml.dom import minidom

sfu_limits = {}

def strip_number(nstr):
    return nstr.replace(" ","").replace(",","").replace(".","")

def forum_search_user(st, ignore_0posts=False, post_filter=-1):
    st = st.replace(" ", "%20")
    try:
        bytes = web.get("https://forum.minetest.net/userlist.php?username=" + st)
        shim = '<tbody>'
        shim2 = '</tbody>'
        if shim in bytes and shim2 in bytes:
            bytes = bytes.split(shim, 1).pop()
            bytes = bytes.split(shim2, 1)[0]
            bytes = shim + bytes + shim2 # Root Tag needed
            dom = minidom.parseString(bytes)
            l = dom.getElementsByTagName("td")
            users = []
            idx = 0
            while idx < len(l):
                try:
                    e = not( (ignore_0posts and l[idx+2].firstChild.data == "0") or (post_filter != -1 and int(strip_number(l[idx+2].firstChild.data)) != post_filter) )
                    if e:
                        users.append([l[idx].firstChild.firstChild.data,l[idx+1].firstChild.data,l[idx+2].firstChild.data,l[idx+3].firstChild.data,l[idx].firstChild.getAttribute("href").split("=")[1]])
                    idx += 4
                except:
                    return "Invalid Data"
            return users
        return "No Results found"
    except:
        return "Unknown Error"

def formartirc_user(name,rank,posts,regdate,userid,with_userid=False):
    ap = ""
    if with_userid:
        ap = " | id: " + userid
    if rank.lower() == "administrator":
        return name + " "+chr(3)+"6"+ rank +chr(3)+" " + posts + " posts, registered on " + regdate + ap
    elif rank.lower() == "moderator":
        return name + " "+chr(3)+"9"+ rank +chr(3)+" " + posts + " posts, registered on " + regdate + ap
    elif rank.lower() == "banned":
        return name + " "+chr(3)+"4"+ rank +chr(3)+" " + posts + " posts, registered on " + regdate + ap
    elif rank.lower() == "developer":
        return name + " "+chr(3)+"10"+ rank +chr(3)+" " + posts + " posts, registered on " + regdate + ap
    elif rank.lower() == "new member":
        return name + " "+chr(3)+"8"+ rank.replace("New","New"+chr(3)) +" " + posts + " posts, registered on " + regdate + ap
    else:
	    return name + " " + rank + " " + posts + " posts, registered on " + regdate + ap

def formatirc_user_a(arr):
    if len(arr) <= 4:
        return formartirc_user(arr[0],arr[1],arr[2],arr[3])
    else:
        return formartirc_user(arr[0],arr[1],arr[2],arr[3],arr[4],with_userid=True)

def search_forumuser(phenny, input):
    arg = input.group(2)
    if not arg:
        return phenny.reply("Give me a username")
    ignore_0posts = False
    post_filter = -1
    if " " in arg:
        a = arg.split(" ")
        _args_after_flag = 0
        for i in range(0,len(a)):
            ar = a[i]
            if ar == "-ignore0p":
                ignore_0posts = True
            elif ar.startswith("-p") and ar != "-p": # -p4
                try:
                    post_filter = int(ar[2:])
                except:
                    return phenny.reply("Invalid Number")
            elif ar == "-p": # -p 4
                try:
                    post_filter = int(a[i+1])
                    _args_after_flag = 1
                except IndexError:
                    return phenny.reply("Too few arguments")
                except ValueError:
                    return phenny.reply("Invalid Number")
                except:
                    return phenny.reply("Unknown Error")
            else:
                if _args_after_flag > 0:
                    _args_after_flag -= 1
                else:
                    arg = " ".join(a[i+_args_after_flag:]) # No more Flags found
                    break
    usrs = forum_search_user(arg,ignore_0posts=ignore_0posts,post_filter=post_filter)
    if not type(usrs) == type([]):
        return phenny.reply(usrs)
    else:
        if input.nick in sfu_limits:
            lim = sfu_limits[input.nick]
        elif input.sender.startswith('#'):
            lim = 6
        elif not input.sender.startswith('#'):
            lim = 25
        if len(usrs) > lim:
            return phenny.reply("Too many matches: %i" % len(usrs))
        else:
            for u in usrs:
                phenny.say(formatirc_user_a(u))


search_forumuser.commands = ['searchforumuser', 'sfu']
search_forumuser.thread = True

def search_forumuser_limit(phenny, input):
    if not input.admin or not input.owner: return
    arg = input.group(2)
    if not arg:
        return phenny.reply("Give me a channel/nickname and a limit")
    elif len(arg.split(" ")) < 2:
        return phenny.reply("Give me a channel/nickname and a limit")
    try:
        if arg.split(" ")[1] == "reset":
            sfu_limits.__delitem__(arg.split(" ")[0])
            phenny.say("Limit reset.")
        else:
            sfu_limits[arg.split(" ")[0]] = int(arg.split(" ")[1])
            phenny.say("Limit set.")
    except:
        return phenny.reply("Error")

search_forumuser_limit.commands = ['searchforumuserlimit', 'sfulimit']
search_forumuser_limit.priority = 'low'

if __name__ == '__main__':
   print(__doc__)
