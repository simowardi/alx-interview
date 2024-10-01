#!/usr/bin/python3
"""Prime Game module:
    Determines the winner between Maria and Ben.
"""


def isWinner(x, nums):
    """Determines the winner after `x` rounds.
    Args:
        x (int): Number of rounds.
        nums (list): Array of `n` values for each round.    
    Returns:
        str: Name of the player with the most wins,
        or None if a tie.
    """
    if x < 1 or not nums:
        return None
    
    marias_wins, bens_wins = 0, 0
    n = max(nums)

    # Generate prime numbers up to the max value in nums
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False

    # Count primes in each round
    for round_num in nums:
        prime_count = sum(primes[1:round_num + 1])
        
        if prime_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
