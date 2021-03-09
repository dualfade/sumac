#!/usr/bin/env python3
# collections --

import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

# parse SharpCollection lists --
def collection_list(self, dnvers, arch):
    """ list SharpCollection exe's """
    print('[+] select a target exe:\n')
    try:
        page = requests.get('https://github.com/Flangvik/SharpCollection/tree/master/NetFramework_%s_%s' % (dnvers, arch))
        page_content = BeautifulSoup(page.content, 'html.parser')
        body = page_content.find_all(class_='js-navigation-open Link--primary')
    except ConnectionError as e:
        print('[!] Error %e' % e)
        sys.exit(-1)

    # populate exe build names --
    e = []
    l, n = collection_info()

    # exe build names --
    for f in body:
        title = f.contents[0]
        e.append(title)

    df = pd.DataFrame({
        "Repository Name": n,
        "Source Code Link": l,
    })
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)
    print('\n[+] select an exe to generate shellcode:\n')
    #print(df.loc[0])

    # return to main --
    return (l, n, e)

# get links --
def collection_info():
    """ get collection link and information -- """
    try:
        page = requests.get('https://github.com/Flangvik/SharpCollection')
        page_content = BeautifulSoup(page.content, 'html.parser')
        body = page_content.find(class_='markdown-body entry-content container-lg')
        name = body.find_all('li')
    except ConnectionError as e:
        print('[!] Error %e' % e)
        sys.exit(-1)

    # populate links / repo names --
    l = []
    n = []

    for f in name:
        href = f.contents[0].get('href')
        text = f.find('a').get_text()
        l.append(href)
        n.append(text)
    return(l, n)
