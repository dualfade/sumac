#!/usr/bin/env python3
# collections --

import re
import sys
import time
import requests
import functools
from bs4 import BeautifulSoup
import pandas as pd

# dataframe class --
class Format_DataFrame:
    """ format dataframe output -- """
    def __init__(self, l, n, e):
        """ link / name / exe -- """
        self.l = l
        self.n = n
        self.e = e

    def format_eframe(self):
        """ executable data -- """
        df_e = pd.DataFrame({
            "Executable Name": self.e,
        })
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df_e)

    def format_lnframe(self):
        """ name / link data -- """
        df_ln = pd.DataFrame({
            "Repository Name": self.n,
            "Repository Link": self.l,
        })
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(df_ln)

# parse SharpCollection exe list --
def collection_list(self, dnvers, arch):
    """ collection exe's by arch and dnn vers --"""
    try:
        page = requests.get('https://github.com/Flangvik/SharpCollection/tree/master/NetFramework_%s_%s' % (dnvers, arch))
        page_content = BeautifulSoup(page.content, 'html.parser')
        body = page_content.find_all(class_='js-navigation-open Link--primary')
    except ConnectionError as e:
        print('[!] Error %e' % e)
        sys.exit(-1)

    # populate exe build names --
    e = []

    # exe build names --
    for f in body:
        title = f.contents[0]
        if (re.search(".exe", title)):
            e.append(title)
        else:
            next

    n, l = collection_info()
    Wrangle_lists(l, e)

    # exectable class --
    #e_out = Format_DataFrame(None, None, e)
    #e_out.format_eframe()

    #return (e)

# sort list data ==
def Wrangle_lists(l, e):
    """ match link / exe names -- """
    """ NaN if not available per build arch -- """
    """ https://bit.ly/3qDLhem """
    lst = []
    for i in e:
        has_match = False
        for j in l:
            if i.split('.')[0] in j:
                has_match = True
                print(i, j)
                if j not in lst:
                    lst.append(j)
            if len(i) > 1:
                k = ' '.join(i.split('.')[:2])
                if k in j:
                    has_match = True
                    print(i, j)
                    if j not in lst:
                        lst.append(j)
        if not has_match:
            lst.append(i + ' - NaN')

# get SharpCollection information --
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

    # populate repo names --
    n = []
    l = []

    for f in name:
        href = f.contents[0].get('href')
        text = f.find('a').get_text()
        l.append(href)
        n.append(text)

    return(n, l)

#__EOF__
