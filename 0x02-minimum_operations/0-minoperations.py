#!/usr/bin/python3
"""Minimum operations solution."""


def minOperations(n):
    """find the minimum number of operations,
    to print n number of characters using the
    operations copy all and past only."""
    if num < 2:
        return 0
    
    operations, divisor = 0, 2
    for divisor in range(2, num + 1):
        while num % divisor == 0:
            operations += divisor
            num //= divisor
        divisor -= 1
    
    return operations