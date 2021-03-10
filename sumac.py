#!/usr/bin/env python3
# sumac --

# refs --
# https://github.com/TheWover/donut
# https://github.com/Flangvik/SharpCollection

# create binary shellcode with random ofuscation

# imports --
import sys
import argparse

from lib.get_collections import collection_info
from lib.get_collections import collection_list
from lib.fetch_collection_exe import fetch_executable

# globals --

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
    information_parser = subparsers.add_parser('info', help='Tell sumac to fetch SharpCollection info list')
    collection_parser = subparsers.add_parser('select', help='Tell sumac to fetch SharpCollection exe list')
    fetch_executable = subparsers.add_parser('fetch', help='Tell sumac to fetch a target SharpCollection exe')

    # do things --
    collection_parser.add_argument('--dnvers', '-d', required=False, default='4.5',
                                   help='Dotnet version (4.0/4.5/4.7) | default: 4.5')
    collection_parser.add_argument('--arch', '-a', required=False, default='x64',
                                   help='Target architecture (x86/x64/any) | default x64')

    # fetch exe -> staging --
    fetch_executable.add_argument('--use', '-u', required=True, help='Fetch target executable')


    # parse the args --
    args = vars(parser.parse_args())

    # set args for fetch --
    try:
        if args['mode'] == 'info':
            print('\n[i] Projects:\n')
            collection_info()
    # select build binary --
        if args['mode'] == 'select':
            print('\n[i] %s Executable list:\n' % args['arch'])
            collection_list('%s, %s',
                                args['dnvers'],
                                args['arch'])
        if args['mode'] == 'fetch':
            print('\n[i] Fetching %s from SharpCollection' % args['use'])

    # exception --
    except Exception as e:
        print('[!] Something puked %e' % e)
        sys.exit(-1)




# __EOF__
