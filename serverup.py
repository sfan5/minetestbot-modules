#!/usr/bin/env python
"""
serverup.py - Minetest-Server Ping Module
Copyright 2012, sfan5
"""

import socket, time

def serverup(phenny, input):
    arg = input.group(2)
    if not arg:
        return phenny.reply("Give me a Server Address")
    if not '.' in arg:
        return phenny.reply("Invalid Address")
    if ':' in arg:
        address = arg.split(':')[0]
        try:
            port = int(arg.split(':')[1])
        except:
            return phenny.reply("Invalid Port")
    else:
        address = arg
        port = 30000
    try:
        start = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2.5)
        buf = "\x4f\x45\x74\x03\x00\x00\x00\x01"
        sock.sendto(buf, (address, port))
        data, addr = sock.recvfrom(1000)
        if data:
            peer_id = data[12:14]
            buf = "\x4f\x45\x74\x03" + peer_id + "\x00\x00\x03"
            sock.sendto(buf, (address, port))
            sock.close()
            end = time.time()
            phenny.reply("%s is up (%0.3fms)" % (arg,end-start))
        else:
            phenny.reply("%s seems to be down " % arg)
    except:
        phenny.reply("%s seems to be down " % arg)

  

serverup.commands = ['up']
serverup.thread = True

if __name__ == '__main__':
    print __doc__
