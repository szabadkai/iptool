from unittest import TestCase

import ipaddr

from iptool.Address import Address


class TestAddress(TestCase):
    def setUp(self):
        self.test_address = Address("128.0.0.1", "255.255.255.000")

    def test_as_network(self):
        self.assertEqual(self.test_address.as_network, ipaddr.IPNetwork("128.0.0.1/24"))

    def test_as_prefixed(self):
        self.assertEqual(self.test_address.as_prefixed, "128.0.0.1/24")

    def test_from_prefixed(self):
        test_network = Address.from_prefixed("128.0.0.1/24")
        self.assertEqual(test_network.as_prefixed, "128.0.0.1/24")
