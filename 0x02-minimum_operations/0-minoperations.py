#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n):
    """
    Minimum operations method
    """
    count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # First copy all and paste
            clipboard = done
            done += clipboard
            count += 2

        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            count += 2

        elif clipboard > 0:
            # Paste
            done += clipboard
            count += 1

    return count
