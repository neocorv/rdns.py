#!/usr/bin/env python
import urllib2, sys, re
from bs4 import BeautifulSoup as bs4

dmn = sys.argv[1]
req = urllib2.urlopen('http://viewdns.info/iphistory/?domain=' + dmn)
res = req.read()
sou = bs4(res, 'html.parser')
rgx = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
fnl = []

for ent in sou.findAll('td'):
	if rgx.match(ent.text):
		fnl.append(ent.text)

fnl = list(set(fnl))

for ent in fnl:
print (ent)
