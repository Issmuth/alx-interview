#!/usr/bin/python3
"""Minimum operations solution."""


def minOperations(n):
    """find the minimum number of operations,
    to print n number of characters using the
    operations copy all and past only."""
    if n < 2:
        return 0
    
    ops, divs = 0, 2
    for divs in range(2, n + 1):
        while n % divs == 0:
            ops += divs
            n //= divs
        divs -= 1
    
    return ops