#!/usr/bin/python

from pprint import pprint
import requests
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='url of subreddit')
args = parser.parse_args()

r = requests.get(args.url + '/.json',
                 headers = {'User-agent': 'your bot 0.1'})

if r.ok:
    print "Download successful"
else:
    print "Error ", r.status_code
    exit(r.status_code)

data = r.json()
print data['data']['children'][0]['data']['title']
