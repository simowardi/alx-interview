#!/usr/bin/python3
"""
This module provides a function to validate if a list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Function to check if a list of integers represents a valid UTF-8 encoding.

    Args:
    data (list of int): A list of integers where each
                    integer represents a byte of data.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to identify the leading byte of a UTF-8 character
    # and to identify bytes (which should start with 10)
    mask1 = 1 << 7   # 10000000 in binary
    mask2 = 1 << 6   # 01000000 in binary

    # Loop over each integer (byte) in the data
    for byte in data:

        # Mask to check the most significant bit (MSB)
        mask = 1 << 7

        # If we are expecting more bytes in the UTF-8 character
        if num_bytes == 0:
            # Determine how many bytes are in this UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If num_bytes is 0, it means it's a 1-byte character
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4, it's not valid UTF-8
            if num_bytes > 4:
                return False

            # We need to check the remaining num_bytes - 1 bytes
            num_bytes -= 1
        else:
            # Check if the byte is a continuation byte
            # it should start with 10
            if not (byte & mask1 and not (byte & mask2)):
                return False
            # One less byte to check
            num_bytes -= 1

    # If num_bytes is not zero,
    # it means there are leftover bytes, so it's invalid
    return num_bytes == 0
