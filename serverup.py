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
        return phenny.reply("Note: Syntax changed please use 'example.org 1337' instead of 'example.org:1337'")
    if ' ' in arg:
        address = arg.split(' ')[0]
        port = arg.split(' ')[1]
        if '-' in port or ',' in port:
            ports = []
            ports_ = port.split(',')
            for p in ports_:
                if '-' in p:
                    if len(p.split('-')) != 2:
                        return phenny.reply("Invalid Port List")
                    else:
                        try:
                            a = int(p.split('-')[0])
                        except:
                            return phenny.reply("Invalid Port: %s" % p.split('-')[0])
                        try:
                            b = int(p.split('-')[1]) + 1
                        except:
                            return phenny.reply("Invalid Port: %s" % p.split('-')[1])
                        for i in range(a, b):
                            ports.append(i)
                else:
                    try:
                        ports.append(int(p))
                    except:
                        return phenny.reply("Invalid Port: %s" % p)
        else:
            try:
                ports = [int(port)]
            except:
                return phenny.reply("Invalid Port: %s" % port)
    else:
        address = arg
        ports = [30000]
    if len(ports) > 4 and not (input.admin or input.owner): # Owner and Admins of the Bot can bypass the Limit
        return phenny.reply("Too many Ports specified")
    for port in ports:
        repres = address + ':' + str(port)
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
                phenny.say("%s is up (%0.3fms)" % (repres,end-start))
            else:
                phenny.say("%s seems to be down " % repres)
        except:
            phenny.say("%s seems to be down " % repres)

  

serverup.commands = ['up']
serverup.thread = True

if __name__ == '__main__':
    print __doc__
