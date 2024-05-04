#!/usr/bin/python3
"""
Making change module
"""


def makeChange(coins, total):
    """
    Make change function
    """
    if total <= 0 or min(coins) > total or coins == []:
        return 0
    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            change += 1

    if total != 0:
        return -1

    return change
