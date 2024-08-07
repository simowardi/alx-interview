#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n H characters.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.
    
    Args:
    n (int): The desired number of H characters
    
    Returns:
    int: The minimum number of operations, or 0 if n is impossible to achieve
    """
    # Check if n is a valid input (positive integer greater than 1)
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0  # Counter for the number of operations
    clipboard = 0   # Content of the clipboard (number of H's copied)
    current_h = 1   # Current number of H's in the file (starts with 1 H)

    while current_h < n:
        # If clipboard is empty or copying all would be more efficient
        if clipboard == 0 or n - current_h < clipboard:
            # Perform Copy All operation
            clipboard = current_h
            operations += 1
        
        # If pasting won't exceed the target n
        if n - current_h >= clipboard:
            # Perform Paste operation
            current_h += clipboard
            operations += 1
        
        # Check if we've reached the target
        if current_h == n:
            return operations

    # This line is reached if n is impossible to achieve
    return 0
