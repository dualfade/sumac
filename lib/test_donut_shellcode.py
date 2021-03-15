#!/usr/bin/env python3
# donut shellcode test --
# https://pypi.org/project/donut-shellcode/

import sys
import donut
import time
import subprocess

def create(self, file):
    """ create donut shellcode -- """
    # parse args --

    # donut args --
    sc = donut.create(file='%s' % file)

    # subprocess run --
    sc_generate = subprocess.run(['%s' % sc],
                                     stdin=None, stdout=None, stderr=None, shell=False)
    print('\n[+] Shellcode generated: %d' %sc_generate.returncode)
