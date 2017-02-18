#!/usr/bin/python

from pprint import pprint
import requests
import json

r = requests.get(r'http://www.reddit.com/r/worldnews/.json',
                 headers = {'User-agent': 'your bot 0.1'})

if r.ok:
    print "Download successful"
else:
    print "Error ", r.status_code
    exit(r.status_code)

data = r.json()
print data['data']['children'][0]['data']['title']
