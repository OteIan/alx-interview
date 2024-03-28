#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys


line_count = 0
total_file_size = 0
status_code_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}


def print_metrics(status_code_count, total_file_size):
    """
    Prints the metrics including total file size and the number of lines for
    each status code.

    Args:
        status_code_count (dict): Dictionary containing status codes as keys
        and their counts as values.
        total_file_size (int): Total file size accumulated so far.
    """
    print(f"File size: {total_file_size}")
    for code, number in sorted(status_code_count.items()):
        if number > 0:
            print(f"{code}: {number}")


try:
    # Read stdin line by line
    for line in sys.stdin:
        output = line.split()

        # Checks if stdin is in the correct format
        if len(output) > 2:
            line_count += 1  # Updates line count

            status_code = output[-2]
            total_file_size += int(output[-1])  # Updates total file size

            # Updates the status code dictionary
            if status_code in status_code_count.keys():
                status_code_count[status_code] += 1

            if line_count % 10 == 0:
                # Print metrics after every 10 lines
                print_metrics(status_code_count, total_file_size)

finally:
    # Print the final metrics if Ctrl+C is called
    print_metrics(status_code_count, total_file_size)
