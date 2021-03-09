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

.▄▄ · ▄• ▄▌• ▌ ▄ ·.  ▄▄▄·  ▄▄· 
▐█ ▀. █▪██▌·██ ▐███▪▐█ ▀█ ▐█ ▌▪
▄▀▀▀█▄█▌▐█▌▐█ ▌▐▌▐█·▄█▀▀█ ██ ▄▄
▐█▄▪▐█▐█▄█▌██ ██▌▐█▌▐█ ▪▐▌▐███▌
 ▀▀▀▀  ▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀ ·▀▀▀
                    @dualfade
          ''')

# main --
if __name__ == "__main__":
    banner()

    # args --
    parser = argparse.ArgumentParser(prog='sumac')
    subparsers = parser.add_subparsers(dest='mode', help='sumac prog functions')
    collection_parser = subparsers.add_parser('fetch', help='Tell sumac to fetch SharpCollection list')

    collection_parser.add_argument('--dnvers', required=False, default='4.5', help='Dotnet version (4.0/4.5/4.7)')
    collection_parser.add_argument('--arch', required=False, default='x64', help='Target architecture (x86/x64/any)')

    # parse the args --
    args = vars(parser.parse_args())

    # set args for fetch --
    if args['mode'] == 'fetch':
        l, n, e = collection_list('%s, %s', 
                                  args['dnvers'],
                                  args['arch'])
