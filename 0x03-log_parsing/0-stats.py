#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_parts = line.split()
        if len(line_parts) > 4:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_file_size += file_size
            line_count += 1

        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_file_size))
            for code, count in sorted(status_codes.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_codes.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
