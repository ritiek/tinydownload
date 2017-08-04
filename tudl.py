#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import os
import sys

file_id = sys.argv[1]

response = requests.get('http://s000.tinyupload.com/?file_id=' + file_id)
soup = BeautifulSoup(response.text, 'html.parser')

for x in soup.find_all('a'):
    if x['href'].startswith('download.php'):
        full_link = 'http://s000.tinyupload.com/' + x['href']
        print(full_link)
        ffmpeg_bin = requests.get(full_link, stream=True)
        with open('download', 'wb') as handle:
            for block in ffmpeg_bin.iter_content(1024):
                handle.write(block)
