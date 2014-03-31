#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_puck
----------------------------------

Tests for `puck` module.
"""

import unittest

from puck import enebriate

class Enebriate(unittest.TestCase):
    def test_something(self):
        """
        How on earth do you test this?
        """
        sequence = ['a', 'b', 'c', 'd']
        for idx, el in enebriate(sequence):
            self.assertIn(el, sequence)


if __name__ == '__main__':
    unittest.main()
