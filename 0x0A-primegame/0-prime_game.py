#!/usr/bin/python3
"""
Prime game module
"""


def isWinner(x, nums):
    """
    Prime game method
    """
    if x < 1 or not nums:
        return None

    m_wins, b_wins = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n+1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i+i, n+1, i):
            primes[j-1] = False

    for _, n in zip(range(x), nums):
        count = len(list(filter(lambda x: x, primes[0: n])))
        b_wins += count % 2 == 0
        m_wins += count % 2 == 1

    if m_wins == b_wins:
        return None

    if m_wins > b_wins:
        return 'Maria'
    else:
        return 'Ben'
