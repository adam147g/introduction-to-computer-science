#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from for_imports import *

from basics import repeat


class TestRepeat(unittest.TestCase):
    def test_squared(self):
        self.assertListEqual([1, 9, 25], repeat(lambda x: x ** 2))


if __name__ == '__main__':
    unittest.main()
