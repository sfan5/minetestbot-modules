#!/usr/bin/env python
"""
shortutil.py - Phenny Custom Shortcut Module
Copyright 2013 jmf
Licensed under the WTFPL.
http://www.wtfpl.net/txt/copying/

Module for phenny:
http://inamidst.com/phenny/
"""

import random
import web
import re

def make_cmd(cmd, txt):
  def m(phenny, input):
    t = txt
    if input.group(2):
      u = input.group(2).strip() + ", "
    else:
      u = ""
      t = t[0].upper() + t[1:]
    phenny.say(u + t)
  m.commands = [cmd]
  return m

rtfm = make_cmd("rtfm", "someone thinks you should read the manual. The development wiki is at http://dev.minetest.net, the regular wiki is at http://wiki.minetest.net.")
questions = make_cmd("questions", "someone thinks that your question is inaccurate or doesn't follow the guidelines. Read the guidelines here: http://catb.org/~esr/faqs/smart-questions.html")
pil = make_cmd("pil", "someone thinks you need to brush up on or learn Lua, please go to: http://lua.org/pil/")
git = make_cmd("git", "someone thinks you need to brush up on or learn Git, please go to: http://git-scm.com/book/")
stfu = make_cmd("stfu", "someone thinks you need to shut the fuck up before you get muted.")
proc = make_cmd("proc", "someone thinks you need to stop procrastinating.")

def next(phenny, input):
   """Next one please"""
   phenny.say("Another satisfied customer. Next!")

next.commands = ['next']

def doge(phenny, input):
	"""much wow, very function, such programming"""
	links = [
		"http://is.gd/zgopNT", # http://fc09.deviantart.net/fs70/f/2014/002/d/f/wow_by_kawiku-d70lb8q.png
		"http://i.imgur.com/JphfPur.jpg",
		"http://i.imgur.com/2MmvpGR.jpg",
		"https://people.mozilla.org/~smartell/meme/such-logo.gif",
		"http://i.imgur.com/e16WWlK.gif",
		"http://i.imgur.com/6wx9Mf9.png",
		"http://i.imgur.com/1GVIKve.jpg",
		"http://i.imgur.com/606BPbS.png",
		"http://i.imgur.com/VcwHcBO.jpg",
		"http://i.imgur.com/3pnQciA.jpg",
		"http://i.imgur.com/ampdE1n.jpg",
		"http://i.imgur.com/QIqDXZw.gif",
		"http://i.imgur.com/PoYoFXg.jpg",
		"http://i.imgur.com/xcrvGLn.jpg",
		"http://25.media.tumblr.com/282b439e00e13be63e932425388afa7d/tumblr_muopr4oEjG1qbhxqdo1_1280.jpg",
		"http://i.imgur.com/EW37mvz.jpg",
		"http://i.imgur.com/F2vYL4j.gif",
		"http://25.media.tumblr.com/5b1de230c236cbc6310ae000e1a5cdc2/tumblr_mu7uxmD9i31rdj00zo1_500.jpg",
		"http://i.imgur.com/Ck3qYFb.jpg",
		"http://i.imgur.com/wp9x7GY.gif",
		"https://pp.vk.me/c607929/v607929263/624e/K6NMxz0Cj7U.jpg",
		"http://i.imgur.com/q7VKiiK.gif",
		"http://i.imgur.com/RKHNg3v.jpg",
		"http://i.imgur.com/l0YSsre.jpg",
		"http://i.imgur.com/YRdsSHn.jpg",
		"http://i.imgur.com/HhjNnIX.png",
		"http://i.imgur.com/qLbktNN.jpg",
		"http://i.imgur.com/NOIyL1K.jpg",
		"http://i.imgur.com/v7gjzme.jpg",
		"http://i.imgur.com/uI51MQy.png",
		"http://i.imgur.com/JBXo2M5.jpg",
		"https://i.imgur.com/lpdPpxX.jpg",
	]
	# ^ How to be productive on a Saturday
	phenny.say(random.choice(links))

doge.commands = ['doge']

def cat(phenny, input):
	cats = [
		"meow :3",
		"http://i.imgur.com/qmj3sTy.jpg",
		"http://i.imgur.com/iEyDY2z.jpg",
		"http://i.imgur.com/BY5ehYX.jpg",
		"http://i.imgur.com/D448EQt.jpg",
		"http://i.imgur.com/3l1REu3.jpg",
		"http://i.imgur.com/3012uP2.jpg",
		"http://i.imgur.com/0p9arhp.jpg",
		"http://i.imgur.com/c6nvxLE.jpg",
		"http://i.imgur.com/ERebecg.jpg",
		"http://i.imgur.com/AU5LoAs.jpg",
		"http://i.imgur.com/RoCxCms.jpg",
		"http://i.imgur.com/CkgC24b.jpg",
		"http://i.imgur.com/iATkdQO.jpg",
		"http://i.imgur.com/kA8l8oP.jpg",
		"http://i.imgur.com/BIPTRoc.jpg",
		"http://i.imgur.com/bjM2UlX.jpg",
		"http://i.imgur.com/YMm7Tgl.jpg",
		"http://i.imgur.com/qNBpvF3.jpg",
		"http://i.imgur.com/CjNrx6g.jpg",
		"http://i.imgur.com/XaU5D0a.jpg",
		"http://i.imgur.com/F1JBD2m.jpg",
		"http://i.imgur.com/q4RPFjJ.jpg",
		"http://i.imgur.com/fVK8nca.jpg",
		"http://i.imgur.com/bZiCFie.jpg",
		"http://i.imgur.com/MSLjnAw.jpg",
		"http://i.imgur.com/DCXEhOJ.jpg",
		"http://i.imgur.com/gfPVdsc.jpg",
		"http://i.imgur.com/i78Jltr.jpg",
		"http://i.imgur.com/R18cQmP.png",
		"http://i.imgur.com/0ekIBPl.jpg",
		"http://i.imgur.com/foNWNCA.jpg",
		"http://i.imgur.com/NCpnwbx.jpg",
		"http://i.imgur.com/NKWGj9s.jpg",
		"http://i.imgur.com/6tZDQQn.jpg",
		"http://i.imgur.com/7jtdgLn.jpg",
		"http://i.imgur.com/hF7WuV9.jpg",
		"http://i.imgur.com/A6Pw3Cf.jpg",
		"http://i.imgur.com/9tHeEYj.jpg",
		"http://i.imgur.com/f6q50SJ.jpg",
		"http://i.imgur.com/3nHDsb8.jpg",
		"http://i.imgur.com/w9c7A6x.jpg",
		"http://i.imgur.com/rBJgj7d.jpg",
		"http://i.imgur.com/TC7fv.jpg",
		"http://i.imgur.com/xRPBWSw.jpg",
		"http://i.imgur.com/qjzMvkJ.jpg",
		"http://i.imgur.com/qYdPjox.jpg",
		"http://i.imgur.com/8UvDsPc.jpg",
		"http://i.imgur.com/yFmko1j.jpg",
		"https://i.imgur.com/kQ62yNM.jpg",
		"https://i.imgur.com/s9tdEOi.jpg",
		"http://i.imgur.com/8mFITRO.jpg",
		"http://i.imgur.com/ZT2jVRu.jpg",
		"http://i.imgur.com/NIwzCXd.jpg"
	]
	phenny.say(random.choice(cats))

cat.commands = ['cat']

def btc(phenny, input):
	"""Get current Bitcoin price"""
	data, sc = web.get('https://blockchain.info/ticker')
	data = str(data, 'utf-8')
	data = web.json(data)
	if input.group(2):
		currency = input.group(2).strip().upper()
	else:
		currency = 'USD'
	if not currency in data.keys():
		return phenny.reply('Unknown currency. Supported currencies: ' + ', '.join(data.keys()))
	phenny.say('1 BTC = %.4f %s' % (data[currency]['15m'], data[currency]['symbol']))

btc.commands = ['btc']

def resolve_generators(arr):
	out = []
	generator = type(_ for _ in [])
	for e in arr:
		if type(e) == generator:
			for ee in e:
				out.append(ee)
		else:
			out.append(e)
	return out

def combine(phenny, input):
	if not input.group(2): return
	combiners = [
		(chr(n) for n in range(0x0300, 0x034e + 1)),
		(chr(n) for n in range(0x0350, 0x0362 + 1)),
		(chr(n) for n in range(0x1dc0, 0x1dca + 1)),
		"\u1dfe", "\u1dff", 
		(chr(n) for n in range(0xfe20, 0xfe23 + 1)),
	]
	combiners = resolve_generators(combiners)
	o = input.group(2)[0]
	for char in input.group(2)[1:]:
		o += random.choice(combiners) + char
	phenny.say(o)
	
combine.commands = ['combine']

def resadj(phenny, input):
	# Search for n so that n * factor == int(n * factor) starting from iv, adding delta each step (max 500)
	def dothing(iv, delta, factor):
		v = iv
		i = 0
		while i < 500:
			n = v * factor
			if int(n) == n:
				return v
			v += delta
			i += 1
		return -1
	args = input.group(2).split(" ")
	if len(args) < 3:
		return phenny.reply("Usage: resadj <original res.> <aspect ratio> <w or h>")
	if not re.match(r'^\d+x\d+$', args[0]):
		return phenny.reply("fix your args")
	if not re.match(r'^\d+:\d+$', args[1]):
		return phenny.reply("fix your args")
	w, h = (int(args[0].split("x")[0]), int(args[0].split("x")[1]))
	ar = (int(args[1].split(":")[0]), int(args[1].split(":")[1]))
	res = ""
	if args[2].lower() == "w":
		f = ar[1] / ar[0]
		n = dothing(w, 1, f)
		res += "\u2191 "
		if n == -1:
			res += "???"
		else:
			res += "%dx%d (diff=%d)" % (n, n * f, n - w)
		res += " | "
		n = dothing(w, -1, f)
		res += "\u2193 "
		if n == -1:
			res += "???"
		else:
			res += "%dx%d (diff=%d)" % (n, n * f, w - n)
	elif args[2].lower() == "h":
		f = ar[0] / ar[1]
		n = dothing(h, 1, f)
		res += "\u2191 "
		if n == -1:
			res += "???"
		else:
			res += "%dx%d (diff=%d)" % (n * f, n, n - h)
		res += " | "
		n = dothing(h, -1, f)
		res += "\u2193 "
		if n == -1:
			res += "???"
		else:
			res += "%dx%d (diff=%d)" % (n * f, n, h - n)
	else:
		return phenny.reply("fix your args")
	phenny.say(res)

resadj.commands = ['resadj', 'resadjust']

