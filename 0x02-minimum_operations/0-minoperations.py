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
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    current_h = 1
    
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
        
        if n == 1:
            break

    return operations
