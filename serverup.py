#!/usr/bin/env python3
"""
serverup.py - Minetest server ping module
Copyright 2018, sfan5
Licensed under GNU General Public License v2.0
"""
import socket
import time

def check(host, port):
    try:
        ai = socket.getaddrinfo(host, port, proto=socket.IPPROTO_UDP)[0]
    except socket.gaierror:
        return None, "host did not resolve"
    if all(c in "0123456789." for c in host) or ":" in host:
        ipproto = "" # is obvious to the user
    else:
        ipproto = "IPv6" if ai[0] == socket.AF_INET6 else "IPv4"

    sock = socket.socket(*ai[:3])
    sock.settimeout(2.0)
    sock.connect(ai[4])
    try:
        # ask for a peer id
        sock.send(b"\x4f\x45\x74\x03\x00\x00\x00\x01")
        start = time.time()
        data = sock.recv(1024)
        if not data:
            return None, ipproto
        end = time.time()
        # disconnect again
        peer_id = data[12:14]
        sock.send(b"\x4f\x45\x74\x03" + peer_id + b"\x00\x00\x03")
        return end - start, ipproto
    except socket.error:
        return None, ipproto
    finally:
        sock.close()

def serverup(phenny, input):
    arg = input.group(2).strip()
    if not arg:
        return phenny.reply("give me an address and (optionally) a port")

    if '.' in arg: # IPv4 or a domain name
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

    if port < 1024 and port >= 2**16:
        return phenny.reply("invalid port")

    if ":" in address:
        desc = "[%s]:%d" % (address, port)
    else:
        desc = "%s:%d" % (address, port)
    result, extra = check(address, port)
    if result is None:
        msg = "%s seems to be down" % desc
    else:
        msg = "%s is up (%dms)" % (desc, result*1000)
    if extra != "":
        msg += " (%s)" % extra
    phenny.say(msg)

serverup.commands = ['up']

if __name__ == '__main__':
    print(__doc__)
