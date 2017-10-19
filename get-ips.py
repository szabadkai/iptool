#!/usr/bin/env python3

import argparse

from iptool.AddressService import AddressService

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--with-prefix', action='store_true', default=False)
parser.add_argument('--overlaping', action='store_true', default=False)
args = parser.parse_args()

addrs = AddressService.get_addrs()

if args.with_prefix and not args.overlaping:
    print("\n".join(sorted(a.as_prefixed for a in addrs)))
elif args.overlaping:
    print(
        "\n\n".join(sorted(a[0].as_prefixed + "\n" + a[1].as_prefixed for a in AddressService.get_overlapping(addrs))))
else:
    print("\n".join(sorted(str(a) for a in addrs)))
