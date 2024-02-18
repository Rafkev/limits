def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [num for num, is_prime in enumerate(primes) if is_prime]
    return prime_numbers

# Example usage
if __name__ == "__main__":
    limit = 50
    primes = sieve_of_eratosthenes(limit)
    print(f"Prime numbers up to {limit}: {primes}")
