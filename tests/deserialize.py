#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2015 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals


import unittest
from btctxstore import deserialize
from btctxstore import exceptions


class TestNulldataTxOut(unittest.TestCase):

    def test_max_data(self):
        # fourty bytes ok
        max_data = 40 * b"aa"
        deserialize.nulldatatxout(max_data)

        # > fourty bytes fails
        def callback():
            over_max_data = 41 * "aa"
            deserialize.nulldatatxout(over_max_data)
        self.assertRaises(exceptions.MaxNulldataExceeded, callback)


class TestKey(unittest.TestCase):

    def test_invalid_netcode(self):
        testnet_wif = "cNf7CMEHfD2jLtiTASbCAEneVnVmD4syA4A9KhUXqAkRs26Ke6xw"
        mainnet_wif = "KzU3561hXZwFPrzmHkJ6FLWvykFJMQnMEwSKXW5VPpz6HcxuvpZq"

        # test positive
        deserialize.key(True, testnet_wif) # testnet
        deserialize.key(False, mainnet_wif) # mainnet

        # testnet negative
        def callback():
            deserialize.key(False, testnet_wif)
        self.assertRaises(exceptions.InvalidWif, callback)

        # mainnet negative
        def callback():
            deserialize.key(True, mainnet_wif)
        self.assertRaises(exceptions.InvalidWif, callback)


class TestAddress(unittest.TestCase):

    def test_invalid_netcode(self):
        testnet_address = "mgBJ5bG9mQw8mHHcVEJghMamQEXeNLtvpt"
        mainnet_address = "1BTF7gU1EmgasGh85ypacDvsVKg4weZMfz"

        # testnet positive
        address = deserialize.address(True, testnet_address)
        self.assertEqual(testnet_address, address)

        # mainnet positive
        address = deserialize.address(False, mainnet_address)
        self.assertEqual(mainnet_address, address)

        # testnet negative
        def callback():
            deserialize.address(False, testnet_address)
        self.assertRaises(exceptions.InvalidAddress, callback)

        # mainnet negative
        def callback():
            deserialize.address(True, mainnet_address)
        self.assertRaises(exceptions.InvalidAddress, callback)
