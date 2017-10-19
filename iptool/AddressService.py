from itertools import combinations
from netifaces import interfaces, ifaddresses, AF_INET

from iptool.Address import Address


class AddressService:
    @staticmethod
    def get_addrs():
        addresses = []
        for ifaceName in interfaces():
            for i in ifaddresses(ifaceName).setdefault(AF_INET, []):
                if i:
                    addresses.append(Address(i['addr'], i['netmask']))
        return addresses

    @staticmethod
    def get_overlapping(addresses):
        pairs = combinations(addresses, 2)
        return (i for i in pairs if i[0].as_network.overlaps(i[1].as_network))
