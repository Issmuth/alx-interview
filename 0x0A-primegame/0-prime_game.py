#!/usr/bin/python3
"""Prime Game - Maria and Ben's game implementation"""

def determine_winner(rounds, numbers):
    """
    Determines the winner after a series of rounds.
    
    rounds: Number of rounds to play
    numbers: List of maximum numbers for each round
    """
    if rounds <= 0 or not numbers or rounds != len(numbers):
        return None

    maria_score = 0
    ben_score = 0

    max_num = max(numbers)
    prime_flags = [True] * (max_num + 1)
    prime_flags[0], prime_flags[1] = False, False
    for i in range(2, int(max_num**0.5) + 1):
        if prime_flags[i]:
            mark_non_primes(prime_flags, i)

    for num in numbers:
        prime_count = sum(prime_flags[:num + 1])
        if prime_count % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None


def mark_non_primes(prime_flags, prime):
    """
    Marks the multiples of a prime number as non-prime.
    
    prime_flags: List indicating whether numbers are prime
    prime: The prime number whose multiples need to be marked
    """
    for multiple in range(prime * prime, len(prime_flags), prime):
        prime_flags[multiple] = False
