#!/usr/bin/python3
"""Least number of coins in change."""


def makeChange(coins, total):
    """returns the least number
    of coins needed for change."""
    coinsCount = 0

    coins.sort()

    i = len(coins) - 1
    while total > 0 and i >= 0:
        if total % coins[i] == 0:
            return int((total / coins[i]) + coinsCount)

        total -= coins[i]
        coinsCount += 1

        if coins[i] > total:
            i -= 1

    if total < 0:
        return -1

    return int(coinsCount)
