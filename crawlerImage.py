# Program by RickyCga, 11/14/2016
# This program is for crawling image from google image search.

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as bs
import os
import argparse

# Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keyword", required=True,
                help='keyword like: walking-people')
args = vars(ap.parse_args())

# Search KeyWord from argument KEYWORD
keyWord = args["keyword"].replace('-', ' ')
# Setup Dir for storage image
path = './TrainData/' + keyWord
# getsite's path need to add escape to space
escapePath = path.replace(' ', '\ ')

# parse.urlencode value setting
keyWord = urllib.parse.quote(keyWord)
values = {'c2coff': 1, 'safe': 'off', 'hl': 'zh-TW', 'site': 'imghp',
          'tbm': 'isch', 'source': 'hp', 'biw': 1440, 'bih': 803}
kwEncode = urllib.parse.urlencode(values)

# Parse google search source code to get website, and wget it.
try:
    # choose search engine url, and add urlencoded keyword
    url = 'http://www.google.com/search?' + \
        kwEncode + '&q=' + keyWord + '&oq=' + keyWord
    # cheat google that we use as a browser, not a crawler.
    headers = {
        'User-Agent': '(add user Agent info here)'}
    req = urllib.request.Request(url, headers=headers)
    respData = urllib.request.urlopen(req).read()
    imgDiv = bs(respData, 'html.parser').select(
        'div[class="rg_meta"]')
    for imgHttp in imgDiv:
        try:
            imgHttp = imgHttp.get_text().split('":"')[4].split('"')[0]
            getSite = 'wget --directory-prefix=' + escapePath + ' ' + imgHttp
            os.system(getSite)
        except:
            continue

except Exception as e:
    print(str(e))
