#!/usr/bin/python3
"""
This script reads lines from stdin, computes various metrics based on the input format,
and prints the metrics at regular intervals or when a keyboard interrupt is received.
"""
import sys


def print_metrics(total_file_size, status_code_counts):
    """
    Prints the total file size and the number of lines by status code.

    Args:
        total_file_size (int): The total size of all files.
        status_code_counts (dict): A dictionary containing the count of each status code.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        print(f"{status_code}: {status_code_counts[status_code]}")


def parse_log_line(line):
    """
    Extracts the relevant information from a log line.

    Args:
        line (str): A log line in the expected format.

    Returns:
        tuple: A tuple containing the IP address, date, status code, and file size.
        If the line does not match the expected format, None is returned.
    """
    parts = line.strip().split(" ")
    if len(parts) != 9 or parts[2] != '"GET' or parts[4][-1] != '"':
        return None
    ip_address, date, _, status_code, file_size = parts[0], parts[3][1:-1], parts[5], int(parts[6]), int(parts[8][:-1])
    return ip_address, date, status_code, file_size


def main():
    """
    Starts the log parser.
    """
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            log_data = parse_log_line(line)
            if log_data:
                ip_address, date, status_code, file_size = log_data
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_metrics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)


if __name__ == '__main__':
    main()
