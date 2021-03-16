#!/usr/bin/env python3
# sumac --

# refs --
# https://github.com/TheWover/donut
# https://github.com/Flangvik/SharpCollection

# create binary shellcode with random ofuscation

# imports --
import sys
import time
import argparse

from lib import get_collections
from lib import fetch_collection_exe
from lib import test_donut_shellcode

# defs --
def banner():
    print('''

===================================================
==      ===  ====  ==  =====  =====  =======     ==
=  ====  ==  ====  ==   ===   ====    =====  ===  =
=  ====  ==  ====  ==  =   =  ===  ==  ===  =======
==  =======  ====  ==  == ==  ==  ====  ==  =======
====  =====  ====  ==  =====  ==  ====  ==  =======
======  ===  ====  ==  =====  ==        ==  =======
=  ====  ==  ====  ==  =====  ==  ====  ==  =======
=  ====  ==   ==   ==  =====  ==  ====  ===  ===  =
==      ====      ===  =====  ==  ====  ====     ==
===================================================
                                        @dualfade
          ''')

# main --
if __name__ == "__main__":
    banner()

    # args --
    parser = argparse.ArgumentParser(prog='sumac')
    subparsers = parser.add_subparsers(dest='mode', help='sumac functions')
    # genetic list repos info --
    information_parser = subparsers.add_parser('info', help='Tell sumac to fetch SharpCollection url list')
    collection_parser = subparsers.add_parser('select', help='Tell sumac to fetch SharpCollection nightly exe list')
    fetch_parser = subparsers.add_parser('fetch', help='Tell sumac to fetch a target SharpCollection exe')
    donut_parser = subparsers.add_parser('test', help='Generate and test shellcode from a SharpCollection exe')

    # do things --
    collection_parser.add_argument('--dnvers', '-d', required=False, default='4.5',
                                   help='Dotnet version (4.0/4.5/4.7) | default: 4.5')
    collection_parser.add_argument('--arch', '-a', required=False, default='x64',
                                   help='Target architecture (x86/x64/Any) | default x64')

    # fetch exe --
    fetch_parser.add_argument('--dnvers', '-d', required=False, default='4.5',
                                   help='Dotnet version (4.0/4.5/4.7) | default: 4.5')
    fetch_parser.add_argument('--arch', '-a', required=False, default='x64',
                                   help='Target architecture (x86/x64/Any) | default x64')
    fetch_parser.add_argument('--file', '-f', required=True,
                                   help='Target executable to download')

    # create shellcode --
    # https://github.com/TheWover/donut/blob/master/docs/2019-08-21-Python_Extension.md
    donut_parser.add_argument('--infile', '-i', required=True, help='input file')
    donut_parser.add_argument('--arch', '-a', required=False, default=3, type=int, help='arch (int [1..3])')
    donut_parser.add_argument('--format', '-f', required=False, default=1, type=int, help='format (int [1..8])')
    donut_parser.add_argument('--exit', '-x', required=False, default=1, type=int, help='exit func (int [1,2])')
    donut_parser.add_argument('--nsclass', '-n', required=False, help='namespace.class')
    donut_parser.add_argument('--method', '-m', required=False, help='method')
    donut_parser.add_argument('--params', '-p', required=False, help='params')
    donut_parser.add_argument('--output', '-o', required=True, help='output file')


    # parse the args --
    args = vars(parser.parse_args())

    # set args for fetch --
    if args['mode'] == 'info':
        print('\n[i] Projects:\n')
        l = get_collections.collection_info()
        for link in l:
            print('%s' % link)
    # select build binary --
    if args['mode'] == 'select':
        print('\n[i] %s Executable list:\n' % args['arch'])
        get_collections.collection_list('%s, %s',
                            args['dnvers'],
                            args['arch'])
    # fetch exe --
    if args['mode'] == 'fetch':
        print('\n[i] Fetching %s from SharpCollection' % args['file'])
        fetch_collection_exe.fetch_bin('%s, %s, %s',
                                       args['dnvers'],
                                       args['arch'],
                                       args['file'])
    if args['mode'] == 'test':
        print('\n[i] Generating test shellcode from %s' % args['infile'])
        time.sleep(1)
        test_donut_shellcode.create('%s, %d, %d, %d, %s, %s, %s, %s',
                                                args['infile'],
                                                args['arch'],
                                                args['format'],
                                                args['exit'],
                                                args['nsclass'],
                                                args['method'],
                                                args['params'],
                                                args['output'])



# __EOF__
