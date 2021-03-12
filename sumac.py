#!/usr/bin/env python3
# sumac --

# refs --
# https://github.com/TheWover/donut
# https://github.com/Flangvik/SharpCollection

# create binary shellcode with random ofuscation

# imports --
import sys
import argparse

from lib import get_collections
from lib import fetch_collection_exe

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
    fetch_parser.add_argument('--file', '-f', required=True, default='x64',
                                   help='Target executable to download')


    # parse the args --
    args = vars(parser.parse_args())

    # set args for fetch --
    try:
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
        if args['mode'] == 'fetch':
            print('\n[i] Fetching %s from SharpCollection' % args['file'])
            fetch_collection_exe.fetch_bin('%s, %s, %s',
                                           args['dnvers'],
                                           args['arch'],
                                           args['file'])

    # exception --
    except Exception as e:
        print('[!] Something puked %e' % e)
        sys.exit(-1)




# __EOF__
