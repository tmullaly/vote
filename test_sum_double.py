#!/usr/bin/env python3
"""
Unit tests for sum_double.
"""

from __future__ import annotations

import unittest

from sum_double import sum_double


class SumDoubleTests(unittest.TestCase):
    def test_sum_double_with_varied_inputs(self) -> None:
        cases = [
            (1, 2, 3),
            (3, 3, 12),
            (0, 0, 0),
            (-1, 1, 0),
            (-2, -2, -8),
            (5, -5, 0),
            (10, 20, 30),
            (7, 7, 28),
            (100, 1, 101),
            (-3, 4, 1),
        ]
        for left, right, expected in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(sum_double(left, right), expected)


if __name__ == "__main__":
    unittest.main()
