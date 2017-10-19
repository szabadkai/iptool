import ipaddr
import netaddr


class Address:
    def __init__(self, addr, netmask):
        self.addr = addr
        self.prefix = netaddr.IPAddress(netmask).netmask_bits()

    def __eq__(self, other):
        return self.as_prefixed == other.as_prefixed

    @staticmethod
    def from_prefixed(prefixed_ip):
        return Address(netaddr.IPNetwork(prefixed_ip).ip, netaddr.IPNetwork(prefixed_ip).netmask)

    def __str__(self):
        return self.addr

    @property
    def as_network(self):
        return ipaddr.IPNetwork(self.as_prefixed)

    @property
    def as_prefixed(self):
        return "{}/{}".format(self.addr, self.prefix)
