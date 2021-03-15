#!/usr/bin/env python3
# donut shellcode test --
# https://pypi.org/project/donut-shellcode/

import sys
import donut
import time
import subprocess

def create(self, file, arch, nsclass, method, output):
    """ create donut shellcode -- """
    """ our test string -- """
    """ donut -o donut_v0.9.3_Seatbelt.bin -x 2 -c Seatbelt.Program -m Main -p "ARPTable" Seatbelt.exe """

    # parse args --
    sc = donut.create(
        file='{}'.format(file),
        arch=arch,
        cls='{}'.format(nsclass),
        method='{}'.format(method),
        output='{}'.format(output)
    )

    # subprocess run --
    sc_generate = subprocess.run(['%s' % sc],
                                     stdin=None, stdout=None, stderr=None, shell=False)

    # print / run  --
    print('\n[+] Shellcode generated: %d' %sc_generate.returncode)
