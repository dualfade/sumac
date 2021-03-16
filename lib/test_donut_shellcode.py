#!/usr/bin/env python3
# donut shellcode test --
# https://pypi.org/project/donut-shellcode/

import sys
import donut
import base64

# constants --
from .constant import PROGRAM_CS

def create(self, infile, arch, format, exit, nsclass, method, params, output):
    """ create donut shellcode -- """
    shellcode = donut.create(
            file='{}'.format(infile),
            arch=arch,
            format=format,
            exit_opt=exit,
            cls='{}'.format(nsclass),
            method='{}'.format(method),
            params='{}'.format(params),
            output='{}'.format(output)
        )

    # open orig template --
    print('[i] writing -> %s' % output)
    with open ('{}'.format(PROGRAM_CS), 'r') as templ:
        source_templ = templ.read()

    # read bin shellcode / b64 it --
    with open (output, 'rb') as sc_outfile:
        sc_b64 = sc_outfile.read()
        sc_base64 = base64.b64encode(sc_b64)

    # file names --
    atype = arch_type(arch)

    # write base64 payload
    fname_b64 = ".".join(['{}'.format(output), '{}'.format(atype), 'b64'])
    print('[i] writing -> %s' % fname_b64)
    with open ('{}'.format(fname_b64), 'w') as w:
        w.write(str(sc_base64.decode()))

    # replace and write new --
    # will update to use random name /tmp/*.cs --
    fname_cs = ".".join(['{}'.format(output),  '{}'.format(atype), 'cs'])
    print('[i] writing -> %s' % fname_cs)
    updated_templ = source_templ.replace('#replace#', str(sc_base64.decode()), 2)
    with open ('{}'.format(fname_cs), 'w') as newfile:
        newfile.write(updated_templ)

def arch_type(arch):
    """ define arch types -- """
    if arch == 1:
        atype = 'x86'
        return atype
    if arch == 2:
        atype = 'x64'
        return atype
    if arch == 3:
        atype = 'x84'
        return atype
