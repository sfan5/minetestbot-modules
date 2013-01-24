#!/usr/bin/env python
"""
forumutils.py - Phenny Minetest Forum Module
Copyright 2012, Sfan5
"""

import web
from xml.dom import minidom

def forum_search_user(st):
    st = st.replace(" ", "%20")
    try:
        bytes = web.get("http://forum.minetest.net/userlist.php?username=" + st)
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
    usrs = forum_search_user(arg)
    if not type(usrs) == type([]):
        return phenny.reply(usrs)
    else:
        if (len(usrs) > 6 and input.sender.startswith('#')) or (len(usrs) > 25 and not input.sender.startswith('#')):
            return phenny.reply("Too many matches: %i" % len(usrs))
        else:
            for u in usrs:
                phenny.say(formatirc_user_a(u))


search_forumuser.commands = ['searchforumuser', 'sfu']
search_forumuser.thread = True

if __name__ == '__main__':
   print __doc__
