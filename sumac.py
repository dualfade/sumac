#!/usr/bin/env python3
# sumac --

# refs --
# https://github.com/TheWover/donut
# https://github.com/Flangvik/SharpCollection

# create binary shellcode with random ofuscation

# imports --
import sys
import argparse

from lib.get_collections import collection_list

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
    subparsers = parser.add_subparsers(dest='mode', help='sumac prog functions')
    collection_parser = subparsers.add_parser('fetch', help='Tell sumac to fetch SharpCollection repo list')
    select_exe_parser = subparsers.add_parser('select', help='Tell sumac to use a SharpCollection c# exe')

    # get collections  --
    collection_parser.add_argument('--dnvers', '-d', required=False, default='4.5',
                                   help='Dotnet version (4.0/4.5/4.7) | default: 4.5')
    collection_parser.add_argument('--arch', '-a', required=False, default='x64',
                                   help='Target architecture (x86/x64/any) | default x64')

    # list / select exe --
    select_exe_parser.add_argument('--select', '-s', required=False,
                                   help='Select a target binary to generate shellcode')

    # parse the args --
    args = vars(parser.parse_args())

    # set args for fetch --
    try:
        if args['mode'] == 'fetch':
            l, n, e = collection_list('%s, %s', 
                                      args['dnvers'],
                                      args['arch'])
    # select build binary --
        if args['mode'] == 'select':
            print('\nmain placeholder--')

    # exception --
    except Exception as e:
        print('[!] Something puked %e' % e)
        sys.exit(-1)




# __EOF__
