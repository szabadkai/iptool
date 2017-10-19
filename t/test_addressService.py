from unittest import TestCase

from iptool.Address import Address
from iptool.AddressService import AddressService


class TestAddressService(TestCase):
    def test_get_addrs(self):
        self.assertIn(Address.from_prefixed("127.0.0.1/8"), AddressService.get_addrs())

    def test_get_overlapping(self):
        self.assertEqual(list(AddressService.get_overlapping([Address.from_prefixed(a) for a in ['4.5.2.1/22',
                                                                                                 '10.50.60.70/16',
                                                                                                 '127.0.0.1/8']])), [])

        self.assertEqual(list(AddressService.get_overlapping(
            [Address.from_prefixed(a) for a in ['4.5.2.1/22', '4.5.0.3/16']])), [(
            Address.from_prefixed('4.5.2.1/22'),
            Address.from_prefixed('4.5.0.3/16')
        )])
