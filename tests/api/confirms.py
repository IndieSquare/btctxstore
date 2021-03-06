#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2016 Fabian Barkhau <fabian.barkhau@gmail.com>
# License: MIT (see LICENSE file)


from __future__ import print_function
from __future__ import unicode_literals
import os
import unittest
from pycoin.serialize import b2h
from btctxstore import BtcTxStore


CONFIRMED = "6a26d2ecb67f27d1fa5524763b49029d7106e91e3cc05743073461a719776192"
UNCONFIRMED = ""
UNPUBLISHED = b2h(os.urandom(32))


class TestConfirms(unittest.TestCase):

    def setUp(self):
        self.api = BtcTxStore(dryrun=True, testnet=False)

    def test_confirmed(self):
        confirms = self.api.confirms(CONFIRMED)
        self.assertGreater(confirms, 0)

    def test_unconfirmed(self):
        pass  # TODO find always unconfirmed tx and test

    def test_unpublished(self):
        confirms = self.api.confirms(UNPUBLISHED)
        self.assertIsNone(confirms)


if __name__ == '__main__':
    unittest.main()
