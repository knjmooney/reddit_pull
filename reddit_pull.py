#!/usr/bin/python

from pprint import pprint
import requests
import json
import argparse
import urlparse

parser = argparse.ArgumentParser()
parser.add_argument('--subreddit', help='name of subreddit')

args = parser.parse_args()

# Make the construction of the path more intuitive
subreddit_url = 'https://www.reddit.com/'

if args.subreddit:
    subreddit_url = "https://www.reddit.com/r/" + args.subreddit + '/'

response = requests.get(urlparse.urljoin(subreddit_url, '.json'),
                        headers = {'User-agent': 'your bot 0.1'})


if response.ok:
    print "Download successful from", urlparse.urljoin(subreddit_url, '.json')
else:
    print "Error ", response.status_code
    exit(response.status_code)

data = response.json()

# pprint(data['data']['children'][0]['data'])

for i in range(0,3):
    print data['data']['children'][i]['data']['title']
