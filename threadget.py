#!/usr/bin/python

# author hqall 04.01.2011
# retrieves all full-sized images in a 4chan thread and saves them to a new folder
# usage: threadget.py board threadnumber
# example: threadget.py s 12345678
# Original source - http://redd.it/qecdu

import urllib2
import re
import os
import sys
from subprocess import call

# the first parameter has to be the board name
# the second parameter has to be the post number
board = sys.argv[1]
post = sys.argv[2]

sourceUrl = 'http://boards.4chan.org/' + board + '/res/' + post

# the pattern to extract links
pattern = re.compile('http://images\.4chan\.org/' + board + '/src/\d*\.jpg|' + 
    'http://images\.4chan\.org/' + board + '/src/\d*\.png|' +
    'http://images\.4chan\.org/' + board + '/src/\d*\.gif')

# get the html with all the links
response = urllib2.urlopen(sourceUrl)
html = response.read()


matches = pattern.findall(html)

def check_folder(folder):
    if not (os.path.exists(folder)):
        os.mkdir(folder)
    os.chdir(folder)

if matches:
    check_folder(post)
    # uniquify links
    matches = set(matches)
    for currentLink in matches:
        # get the current filename
        p = re.compile('\d*\.jpg|\d*\.png|\d*\.gif')
        print currentLink
        currentFile = p.search(currentLink).group()
        if (os.path.exists(currentFile)):
            print currentFile + " already exists"
        else:
            print "getting " + currentLink
            call("wget " + currentLink + " ", shell=True)

else:
    print "no links found..."