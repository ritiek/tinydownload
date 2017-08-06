#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description='Download files from tinyupload.com')
    parser.add_argument(
        'query',
        metavar='QUERY',
        type=str,
        nargs='*',
        help='the file_id or the tinyupload link')
    parser.add_argument(
        '-n', '--name', default='.',
        required=True,
        help='path and name of the file')
    return parser

def get_file_id(link):
    if not len(link) == 20 and 'tinyupload.com' in link:
        link = link.rstrip('/')
    return link[:-20]

def make_soup(file_id):
    response = requests.get('http://s000.tinyupload.com/?file_id=' + file_id)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_link(soup):
    for x in soup.find_all('a'):
        if x['href'].startswith('download.php'):
            full_link = 'http://s000.tinyupload.com/' + x['href']
            return full_link

def download(link, name):
    download_file = requests.get(full_link, stream=True)
    with open(name, 'wb') as handle:
        for block in download_file.iter_content(1024):
            handle.write(block)

def command_line():
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)
    query = args.query
    name = query.name
    file_id = get_file_id(query)
    soup = make_soup(file_id)
    link = get_link(soup)
    download(link, name)

if __name__ == '__main__':
    command_line()
