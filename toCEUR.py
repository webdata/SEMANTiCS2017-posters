'''
toCEUR: RASH to CEUR rdy HTML5
'''

import sys
import codecs
from bs4 import BeautifulSoup

def removejs(soup):
    
    for script in soup(["script", "style"]):
        script.extract() 
        
    return soup

def removexmlns():
    '''
    xmlns attributes
    '''
    
def metalink():
    '''
    about in meta and link tag
    '''
    
def copycss():
    '''
    put all css and stuff in output folder
    '''
        
def run(path, out):
    # read html file
    f = codecs.open(path, "r", "utf-8")
    
    html = f.read().replace('role=', 'class=')

    # parse html
    soup = BeautifulSoup(html, 'html.parser')
    
    soup = removejs(soup)
    
    #output
    print soup.prettify().encode('utf-8')
    with open(out+"/out.html", "w") as file:
        file.write(str(soup))

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        out = sys.argv[2]
    except IndexError:
        print 'usage: toCEUR.py <path/to/input/html> <path/to/output/folder>'
    run(path, out)

