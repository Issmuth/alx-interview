#!/usr/bin/python3
"""Least number of coins in change."""
import math


def makeChange(coins, total):
    """returns the least number
    of coins needed for change."""
    coinsCount = 0

    if total <= 0:
        return 0

    coins.sort()
    i = len(coins) - 1

    while i >= 0 and total > 0:
        if coins[i] < total:
            coinsCount += math.floor(total / coins[i])
            total = total % coins[i]

        i -= 1

    if total == 0:
        return coinsCount
    else:
        return -1
