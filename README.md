# limits
Python script that implements a mathematical algorithm
This script implements the Sieve of Eratosthenes algorithm, which is an efficient way to find all prime numbers up to a given limit. Here's how it works:

It initializes a list of boolean values indicating whether each number is prime or not.
It starts with the first prime number (2) and marks all multiples of 2 as non-prime.
Then, it moves to the next unmarked number (3) and marks all its multiples as non-prime.
It continues this process until the square of the current prime is greater than the limit.
Finally, it collects all the numbers marked as prime and returns them.
This algorithm has a time complexity of O(n log log n), where n is the limit up to which primes are to be found. It's an example of a mathematical algorithm that uses number theory principles to efficiently solve a problem.
