#!/usr/bin/python3
"""
Making change module
"""


def makeChange(coins, total):
    """
    Make change function
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    i = 0
    change = 0
    length = len(coins)
    while total > 0:
        if length <= i:
            return -1
        if total - coins[i] >= 0:
            total -= coins[i]
            change += 1
        else:
            i += 1

    return change
