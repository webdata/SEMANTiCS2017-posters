#toCEUR

# curl -F "uploaded_file=@MaSQue.html;type=text/html" http://validator.w3.org/check > res.html && firefox res.html

import os
import time
import logging
import requests
import dataset
import sys
import io
import urllib2
import codecs
from lxml import html, etree

def removejs():
    print 'placeholder'
    
def run(path):
    # read html file
    f = codecs.open(path, "r", "utf-8")

    # parse html
    doc = html.fromstring(f)
    
    #print html.tostring(doc)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print 'usage:'
        
    run(path)

