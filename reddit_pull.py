#!/usr/bin/python

from pprint import pprint
import requests
import json
import argparse
import urlparse

parser = argparse.ArgumentParser()
parser.add_argument('--subreddit', help='Name of subreddit', default='popular')
parser.add_argument('--filename' , help='File to print output to',
                    default='pull_output.txt')
parser.add_argument('--number' , help='Number of files to download',
                    default=1, type=int)

args = parser.parse_args()

# Set the subreddit variable
subreddit_url = "https://www.reddit.com/r/" + args.subreddit + '/'

# Request page from reddit
response = requests.get(subreddit_url + '.json',
                        headers = {'User-agent': 'your bot 0.1'})
if not response.ok:
    # print "Download successful from", urlparse.urljoin(subreddit_url, '.json')
# else:
    print "Error ", response.status_code
    exit(response.status_code)

# Parse and print to file
data = response.json()
output_filehandle = open(args.filename, 'w+')
for i in range(0,args.number):
    # print >> output_filehandle, data['data']['children'][i]['data']['title']
    print data['data']['children'][i]['data']['title'],'\n'
