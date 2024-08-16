#!/usr/bin/python3
'''
Log parsing script

This script reads log data from stdin line by line, computes metrics,
and prints statistics after every 10 lines and/or when interrupted.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Output:
- Total file size: sum of all previous file sizes
- Number of lines by status code (in ascending order)

Key Variables:
- status_codes: Dictionary to store count of each status code
- total_file_size: Running sum of all file sizes
- line_count: Counter for number of valid lines processed
'''

import sys

# Initialize dictionaries and variables
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
total_file_size = 0
line_count = 0


def print_statistics():
    '''
    Print the computed statistics:
    - total_file_size: Total file size processed so far
    - status_codes: Count of each status code encountered
    '''
    print('File size: {}'.format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print('{}: {}'.format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1

        # Parse the line
        parts = line.split()
        if len(parts) > 4:
            status_code = parts[-2]
            file_size = parts[-1]

            # Update metrics
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += int(file_size)

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass

finally:
    # Print final statistics
    print_statistics()
