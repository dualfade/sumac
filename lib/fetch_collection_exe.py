#!/usr/bin/env python3
# fetch_colection_exe --

import sys
import request
from tqdm import tqdm

def fetch_executable():
    """ fetch target executable """
    chunk_size = 1024

    url = ''
    req = requests.get(url, stream = True)
    total_size = int(req.headers['content-length'])
    with open("pythontutorial.pdf", "wb") as file:
        for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit='KB'):
            file.write(data)
     
    print("Download Completed !!!")
