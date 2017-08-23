'''
toCEUR: RASH to CEUR rdy HTML5
'''

import sys
import codecs
from selenium import webdriver
from selenium.webdriver import Firefox
from bs4 import BeautifulSoup

def removejs(soup):
    
    for script in soup(["script"]):
        script.extract() 
        
    return soup

def removexmlns(soup):
    '''
    xmlns attributes
    '''
    htmltag = soup.find('html')
    for attribute in ["xmlns:a","xmlns:m","xmlns:mc","xmlns:pic","xmlns:vt","xmlns:wp","xmlns:wps"]:
        del htmltag[attribute]
    return soup
    
def metalink(soup):
    '''
    about in meta and link tag in header
    '''
    for metatag in soup.find('head').findAll('meta'):
        for attribute in ["about"]:
            del metatag[attribute]
    for linktag in soup.find('head').findAll('link'):
        for attribute in ["about"]:
            del linktag[attribute]
    return soup
    
def copyresourcefiles():
    '''
    put all resources in output folder
    '''
    
def generatedSourceHtml():
    '''
    # geckodriver in PATH
    case_url = "file:///home/vehnem/workspace/RASH/SEMANTiCS2017-posters/papers_todo/regular_122_chrysakis/source/submitted_rash/index.html"
    driver = webdriver.Firefox()
    try:
        driver.get(case_url)
        time.sleep(5)
    finally:
        driver.quit()
    '''

def run(path, out):
    # read html file
    f = codecs.open(path, "r", "utf-8")
    
    html = f.read().replace('role=', 'class=')

    # parse html
    soup = BeautifulSoup(html, 'html.parser')
    
    soup = removejs(soup)
    soup = removexmlns(soup)
    soup = metalink(soup)
    
    # output
    # print soup.prettify().encode('utf-8')
    with open(out+"/"+path.replace('/','_'), "w") as file:
        file.write(str(soup))

if __name__ == '__main__':
    # generatedSourceHtml()
    
    try:
        path = sys.argv[1]
        out = sys.argv[2]
    except IndexError:
        print 'usage: toCEUR.py <path/to/input/html> <path/to/output/folder>'
    run(path, out)
    

