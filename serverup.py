#!/usr/bin/env python
"""
serverup.py - Minetest server ping module
Copyright 2014, sfan5
Licensed under GNU General Public License v2.0
"""

import socket, time

def serverup(phenny, input):
    arg = input.group(2)
    if not arg:
        return phenny.reply("give me an address (and port if you want)")
    if not '.' in arg:
        return phenny.reply("invalid address")
    if ':' in arg:
        return phenny.reply("use 'example.org 1337' instead of 'example.org:1337'")
    if ' ' in arg:
        address = arg.split(' ')[0]
        port = arg.split(' ')[1]
        if '-' in port or ',' in port:
            ports = []
            ports_ = port.split(',')
            for p in ports_:
                if '-' in p:
                    if len(p.split('-')) != 2:
                        return phenny.reply("invalid port list")
                    else:
                        try:
                            a = int(p.split('-')[0])
                        except:
                            return phenny.reply("invalid port: %s" % p.split('-')[0])
                        try:
                            b = int(p.split('-')[1]) + 1
                        except:
                            return phenny.reply("invalid port: %s" % p.split('-')[1])
                        for i in range(a, b):
                            ports.append(i)
                else:
                    try:
                        ports.append(int(p))
                    except:
                        return phenny.reply("invalid port: %s" % p)
        else:
            try:
                ports = [int(port)]
            except:
                return phenny.reply("invalid port: %s" % port)
    else:
        address = arg
        ports = [30000]
    if len(ports) != 1 and input.sender.startswith('#') and not (input.admin or input.owner):
        return phenny.reply("to check multiple ports please use private chat")
    if len(ports) > 6 and not (input.admin or input.owner): # owner and admins of the bot can bypass the limit
        return phenny.reply("ow, too many ports!")
    for port in ports:
        repres = address + ':' + str(port)
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(2.5)
            buf = b"\x4f\x45\x74\x03\x00\x00\x00\x01"
            sock.sendto(buf, (address, port))
            start = time.time()
            data, addr = sock.recvfrom(1000)
            if data:
                end = time.time()
                peer_id = data[12:14]
                buf = b"\x4f\x45\x74\x03" + peer_id + b"\x00\x00\x03"
                sock.sendto(buf, (address, port))
                sock.close()
                t = (end - start) * 1000
                phenny.say("%s is up (%dms)" % (repres,t))
            else:
                phenny.say("%s seems to be down " % repres)
        except:
            phenny.say("%s seems to be down " % repres)

serverup.commands = ['up']

if __name__ == '__main__':
    print(__doc__)
