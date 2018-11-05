#!/usr/bin/env python3
"""
serverup.py - Minetest server ping module
Copyright 2018, sfan5
Licensed under GNU General Public License v2.0
"""
import socket
import time

def check(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.0)
    try:
        buf = b"\x4f\x45\x74\x03\x00\x00\x00\x01"
        sock.sendto(buf, (address, port))
        start = time.time()
        data = sock.recv(1024)
        if not data:
            return
        end = time.time()
        peer_id = data[12:14]
        buf = b"\x4f\x45\x74\x03" + peer_id + b"\x00\x00\x03"
        sock.sendto(buf, (address, port))
        sock.close()
        return (end - start)
    except (socket.gaierror, socket.error):
        return

def serverup(phenny, input):
    arg = input.group(2)
    if not arg:
        return phenny.reply("give me an address and port (optional)")

    arg = arg.replace(":", " ")
    if ' ' in arg:
        address, port = arg.split(' ')
        try:
            port = int(port)
        except ValueError:
            return phenny.reply("invalid port")
    else:
        address = arg
        port = 30000

    if '.' not in address:
        return phenny.reply("invalid address")
    if port < 1024 and port >= 2**16:
        return phenny.reply("invalid port")

    desc = "%s:%d" % (address, port)
    result = check(address, port)
    if result is None:
        phenny.say("%s seems to be down" % desc)
    else:
        phenny.say("%s is up (%dms)" % (desc, result*1000))

serverup.commands = ['up']

if __name__ == '__main__':
    print(__doc__)
