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
    divisor = 2     # Start with the smallest prime number
    
    # Continue until n is reduced to 1
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor  # Add the number of operations (Copy All + Paste(s))
            n //= divisor          # Reduce n by dividing it by the divisor
        divisor += 1  # Move to the next potential divisor
        
        # If the square of divisor is greater than n, n is prime
        if divisor * divisor > n:
            if n > 1:
                operations += n  # Add n operations for the remaining prime factor
                break
    
    return operations
