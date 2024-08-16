#!/usr/bin/python3
"""
A script for parsing HTTP request logs and computing various metrics.
"""
import sys
import re


def extract_log_data(log_line):
    """
    Extracts the relevant information from a log line.
    Args:
        log_line (str): A log line in the expected format.
    Returns:
        dict: A dictionary containing the IP address, date, status code,
        and file size.
    """
    log_format = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>[^\]]+)\]\s*',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_pattern = '{}\\-{}{}{}{}\\s*'.format(*log_format)
    match = re.fullmatch(log_pattern, log_line)
    if match:
        return {
            'ip': match.group('ip'),
            'date': match.group('date'),
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return None


def print_metrics(total_file_size, status_code_counts):
    """
    Prints the total file size and the number of lines by status code.
    Args:
        total_file_size (int): The total size of all files.
        status_code_counts (dict): A dictionary containing the count of each
        status code.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_code_counts):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


def update_metrics(log_line, total_file_size, status_code_counts):
    """
    Updates the metrics from a given HTTP request log line.
    Args:
        log_line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_code_counts (dict): A dictionary containing the count of each
        status code.
    Returns:
        int: The new total file size.
    """
    log_data = extract_log_data(log_line)
    if log_data:
        status_code = log_data['status_code']
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        return total_file_size + log_data['file_size']
    return total_file_size


def main():
    """
    Starts the log parser.
    """
    line_count = 0
    total_file_size = 0
    status_code_counts = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line.strip(), total_file_size, status_code_counts
            )
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_code_counts)


if __name__ == '__main__':
    main()
