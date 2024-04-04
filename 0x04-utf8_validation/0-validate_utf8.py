#!/usr/bin/python3
"""
UTF-8 Validation module
"""


def validUTF8(data):
    """
    UTF-8 validation method
    """
    def check(num):
        """
        Checks each value in the list
        """
        mask = 1 << (8 - 1)
        count = 0

        while num & mask:  # Checks the number of leading '1' bits
            mask >>= 1
            count += 1
        return count

    count = 0
    while count < len(data):
        j = check(data[count])
        # Calculates the index of the last byte of the current character
        k = count + j - (j != 0)
        count += 1

        if j == 1 or j > 4 or k >= len(data):
            # Checks if the current integer is invalid
            # If no. of bytes is 1
            # If no. of bytes is more than 4
            # Index of the last byte exceeds length of 'data' list
            return False

        while count < len(data) and count <= k:
            # Checks if any subsequent byte has a number
            # of bytes different from '1'
            current = check(data[count])
            if current != 1:
                return False
            count += 1

        return True
