# The natural brute force algorithm is to iterate over all i from 2 to n , where n is the input to program.
# for each i , we test if i is prime ,if so we add it to result. we can use trivial division to test if i is prime
# by dividing i by each integer from 2 to square root of n.
# Since each test has sqrt(n) time so Total time complexity will be n*sqrt(n) equals to n^(3/2)
# This algorithm does not exploit the fact that we do not need to compute all primes from 1 to n.
# A better approach is to compute the prime and when a number is identified as a prime, to sieve it
# i.e. remove all its multiples up to n from future consideration. We use a boolean array to encode the primes.
import math


def gen_primes(n):
    # since 0 and 1 are not primes
    primes = []
    is_prime = [False, False] + [True for i in range(n - 1)]
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for m in range(p, n + 1, p):
                is_prime[m] = False
    return primes


# The above approach takes (n/2)+(n/3)+(n/5)+(n/7)+..... leading to O(n log log n)
# Optimization
def gen_primes(n):
    # since 0 and 1 are not primes
    primes = []
    is_prime = [False, False] + [True for i in range(n - 1)]
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            primes.append(p)
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
    return primes
