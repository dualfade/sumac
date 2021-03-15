#!/usr/bin/env python3
# donut shellcode test --
# https://pypi.org/project/donut-shellcode/

import sys
import donut
import base64
import subprocess

def create(self, infile, arch, format, exit, nsclass, method, output):
    """ create donut shellcode -- """
    """ our test string -- """
    """ donut -o donut_v0.9.3_Seatbelt.bin -x 2 -c Seatbelt.Program -m Main -p "ARPTable" Seatbelt.exe """

    # parse args --
    sc = donut.create(
        file='{}'.format(infile),
        arch=arch,
        format=format,
        exit_opt=exit,
        cls='{}'.format(nsclass),
        method='{}'.format(method),
        output='{}'.format(output)
    )

    # subprocess  --
    sc_generate = subprocess.check_call(['%s' % sc])
    print('\n[+] Shellcode generated: %d' %sc_generate)
