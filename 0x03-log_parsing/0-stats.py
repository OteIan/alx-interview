#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys


line_count = 0
total_file_size = 0
status_code_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                     "403": 0, "404": 0, "405": 0, "500": 0}

def print_metrics(status_code_count, total_file_size):
    """
    Prints the metrics
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

try:
    for line in sys.stdin:
        output = line.split()

        if len(output) > 2:
            line_count += 1

            if line_count <= 10:
                status_code = output[-2]
                total_file_size += int(output[-1])

                if status_code in status_code_count.keys():
                    status_code_count[status_code] += 1


            if line_count == 10:
                print_metrics(status_code_count, total_file_size)
                line_count = 0
            

except KeyboardInterrupt:
    # Print the metrics if Ctrl+C is called
    print_metrics(status_code_count, total_file_size)

    sys.exit(0)
