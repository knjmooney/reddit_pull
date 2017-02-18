#!/usr/bin/python

from pprint import pprint
import requests
import json
import argparse
import urlparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='url of subreddit')
args = parser.parse_args()

# Make the construction of the path more intuitive
subreddit = 'https://www.reddit.com/'
if args.url:
    subreddit = args.url
response = requests.get(subreddit + '.json',
                        headers = {'User-agent': 'your bot 0.1'})

if response.ok:
    print "Download successful"
else:
    print "Error ", response.status_code
    exit(response.status_code)

data = response.json()
print data['data']['children'][0]['data']['title']
