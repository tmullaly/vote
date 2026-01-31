#!/usr/bin/env python3
"""
Provide a sum_double function for paired integers.
"""

from __future__ import annotations


def sum_double(a: int, b: int) -> int:
    """
    Return the sum of two integers, or double it if they are equal.
    """
    total = a + b
    if a == b:
        return total * 2
    return total


def main() -> int:
    """
    Demonstrate the sum_double function.
    """
    examples = [(1, 2), (3, 3)]
    for left, right in examples:
        print(f"sum_double({left}, {right}) = {sum_double(left, right)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
