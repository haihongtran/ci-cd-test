import unittest
from unittest import TestCase

import numpy


class UnitTest(TestCase):
    def test_pass(self):
        # Pass
        self.assertEqual(numpy.array([1, 2, 3]).sum(), 6)

    @unittest.SkipTest
    def test_fail(self):
        # Fail
        self.fail("Intended fail test.")

    @unittest.SkipTest
    def test_error(self):
        # Error
        raise ValueError("Intended error test.")

    # @unittest.SkipTest
    def test_error_divide_by_0(self):
        # Error
        self.assertEqual(4 / 0, 0)
