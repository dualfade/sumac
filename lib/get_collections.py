#!/usr/bin/env python3
# collections --

import re
import sys
import requests
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
    """ list SharpCollection exe's """
    print('[+] Project Executables:\n')
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

    # exectable class --
    e_out = Format_DataFrame(None, None, e)
    e_out.format_eframe()

    #return (e)

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

    # name / link class --
    ln_out = Format_DataFrame(l, n , None)
    ln_out.format_lnframe()

    #return(n, l)

#__EOF__
