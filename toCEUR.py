'''
toCEUR: RASH to CEUR rdy HTML5
'''

import os
import sys
import codecs
# from selenium import webdriver
# from selenium.webdriver import Firefox
from bs4 import BeautifulSoup
from shutil import copytree, ignore_patterns

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
    
def copyresourcefiles(path, out):
    '''
    put all resources in output folder
    '''
    copytree(path, out, ignore=ignore_patterns('final.html', 'rash.css'))

def copyrashcss(path, out):
    f = codecs.open(path+'/css/rash.css', "r", "utf-8")
    
    replaced = f.read().replace('role=','class=')
    
    with open(out+'/css/rash.css', "w") as file:
        #.encode('ascii', 'xmlcharrefreplace')
        file.write(replaced.encode('utf-8'))
    
    
def nestedlinks(soup):
    '''
    removes nested links
    '''
    for a in soup.findAll('sup'):
        if a.parent.name == 'a':
            link = a.parent['href']
            a.parent.unwrap()
            innerlink = a.find('a')
            innerlink['href']=link
            innerlink['id'] = innerlink['name']
            del innerlink['name'] 
            
    return soup
    
    
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
    f = codecs.open(path+'/final.html', "r", "utf-8")
    
    html = f.read().replace('role=', 'class=')

    # parse html
    soup = BeautifulSoup(html.replace('ISO-8859-1', 'utf-8'), 'html.parser')
    
    soup = removejs(soup)
    soup = removexmlns(soup)
    soup = metalink(soup)
    soup = nestedlinks(soup)
    
    soup.find('footer').decompose()
    
    # output
    copyresourcefiles(path, out)
    copyrashcss(path, out)
    
    with open(out+'/index.html', "w") as file:
        #.encode('ascii', 'xmlcharrefreplace')
        file.write('<!DOCTYPE HTML>\n'+soup.prettify().encode('utf-8'))

if __name__ == '__main__':
    # generatedSourceHtml()
    try:
        path = sys.argv[1]
        out = sys.argv[2]
    except IndexError:
        print 'usage: toCEUR.py <path/to/input/folder> <path/to/output/folder>'
    run(path, out)
    

