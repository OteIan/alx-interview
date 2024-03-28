#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys

line_count = 0
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        # Strip the output into parts
        output = line.strip().split(" ")

        # Obtain the status code and file size
        status_code = int(output[-2])
        file_size = int(output[-1])

        # Increment the line count and total file size
        line_count += 1
        total_file_size += file_size

        # Increment the status code count by 1
        if status_code in status_code_count:
            status_code_count[status_code] += 1

        # Print the metrics after 10 lines of data has been processed
        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_code_count.keys()):
                if status_code_count[code] > 0:
                    print(f"{code}: {status_code_count[code]}")

except KeyboardInterrupt:
    #Print the metrics if Ctrl+C is called
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

    sys.exit(0)
