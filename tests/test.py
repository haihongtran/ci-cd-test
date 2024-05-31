import unittest
from unittest import TestCase

import numpy


class UnitTest(TestCase):
    def test_pass(self):
        # Pass
        self.assertEqual(numpy.array([1, 2, 3]).sum(), 6)

    def test_fail(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_2(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_3(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_4(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_5(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_6(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_7(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_8(self):
        # Fail
        self.fail("Intended fail test.")

    def test_fail_9(self):
        # Fail
        self.fail("Intended fail test.")

    def test_error(self):
        # Error
        raise ValueError("Intended error test.")

    def test_error_2(self):
        # Error
        raise ValueError("Intended error test.")

    def test_error_3(self):
        # Error
        raise ValueError("Intended error test.")

    def test_error_5(self):
        # Error
        raise ValueError("Intended error test.")

    def test_error_6(self):
        # Error
        raise ValueError("Intended error test.")

    def test_error_7(self):
        # Error
        self.assertEqual(4 / 0, 0)

    def test_error_8(self):
        # Error
        self.assertEqual(8 / 0, 0)

    def test_error_9(self):
        # Error
        self.assertEqual(9 / 0, 0)

    def test_error_0(self):
        # Error
        self.assertEqual(0 / 0, 0)
