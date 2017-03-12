#!/usr/bin/python3

import argparse
import json
import requests
import sys

# This function both sets up the command line arguments and then
# parses them before printing to screen
def rp_parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('--subreddit', help='Name of subreddit', default='popular')
    parser.add_argument('--number' , help='Number of files to download',
                        default=1, type=int)
    parser.add_argument('--filename' , help='File to print output to')

    return parser.parse_args()

# Returns a list of the N (N = number_to_download) top titles in
# descending order from subreddit_name.
def rp_get_list_of_subreddit_titles(subreddit_name, number_to_download):
    # Set the subreddit variable
    subreddit_url = "https://www.reddit.com/r/" + subreddit_name + '/'

    # Request page from reddit
    response = requests.get(subreddit_url + '.json',
                        headers = {'User-agent': 'your bot 0.1'})

    if not response.ok:
        print ("Error ", response.status_code)
        exit(response.status_code)

    # Parse and print to file
    data = response.json()
    subreddit_titles = list()

    for i in range(0,number_to_download):
        subreddit_titles.append(data['data']['children'][i]['data']['title'])

    return subreddit_titles

# Main routine, Similar to C/C++, this is the first function run on
# start up of the script.
def main():

    args = rp_parse_command_line()

    subreddit_titles = rp_get_list_of_subreddit_titles(args.subreddit,
                                                       args.number)

    if args.filename is None:
        output_filehandle = sys.stdout
    else:
        # Must set encoding to utf8 in order to print special
        # characters to file
        output_filehandle = open(args.filename,
                                 mode = 'w',
                                 encoding = 'utf8')

    output_text = '\n\n'.join(subreddit_titles)
    output_filehandle.write(output_text)
    output_filehandle.write('\n')

# This is to stop main being run if script is imported into an
# interactive session. (Well I think that's what it does)
if __name__ == '__main__':
    main()
