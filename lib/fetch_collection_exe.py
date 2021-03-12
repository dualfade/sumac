#!/usr/bin/env python3
# fetch_colection_exe --

import sys
import requests
from tqdm import tqdm

# constants --
from .constant import SHARPCOLLECTION_DOWNLOAD

def fetch_bin(self, dnvers, arch, file):
    """ fetch target executable """
    chunk_size = 1024

    # assmeble urls --
    url = ('%s_%s_%s/%s') % (SHARPCOLLECTION_DOWNLOAD, dnvers, arch, file)
    print('[i] Downloads url -> %s' % url)

    try:
        req = requests.get(url, stream = True)
        total_size = int(req.headers['Content-Length'])

        # write file --
        w_file = ('/tmp/%s' % file)
        with open(w_file, "wb") as file:
            for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size),
                             total = total_size/chunk_size, unit='KB'):
                file.write(data)
    except ConnectionError as e:
        print('[!] Download Failed !! %s' % e)
        sys.exit(-1)
     
    print("Download Completed !!!")
