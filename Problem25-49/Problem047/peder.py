from math import sqrt

# Sieve of Erathosthenes
def gen_all_primes_upto(n):
    A = [True] * (n + 1)
    for i in range(2, int(sqrt(n)) + 1):
        if A[i]:
            current_idx = i ** 2
            while current_idx <= n:
                A[current_idx] = False
                current_idx += i
    return filter(lambda x: x != None, [i if A[i] else None for i in range(2, len(A))])

# Originally had Pollard's rho, but it wasn't reliable
def find_prime_factor_naive(number, known_primes):
    for i in known_primes:
        if number % i == 0:
            return i
    return None

# Find lowest factor one at a time until all are found
def find_all_prime_factors(number, known_primes):
    remainder = number
    factors = []
    while remainder not in many_primes_set:
        factor = find_prime_factor_naive(remainder, known_primes)
        factors.append(factor)
        remainder = remainder / factor
    factors.append(remainder)
    return factors

UPPER_LIMIT = 1000000
many_primes = gen_all_primes_upto(UPPER_LIMIT)
many_primes_set = set(many_primes)

consecutives_found = False
memoization = [1, 1, 1]
number = 10
while number < UPPER_LIMIT:
    num_distinct_prev_prev_prev = memoization[0]
    num_distinct_prev_prev = memoization[1]
    num_distinct_prev = memoization[2]
    num_distinct = len(set(find_all_prime_factors(number, many_primes)))
    if num_distinct_prev_prev_prev == 4 and num_distinct_prev_prev == 4 and num_distinct_prev == 4 and num_distinct == 4:
        print("{}, {}, {}, {}".format(number - 3, number - 2, number - 1, number))
        break
    memoization[0] = num_distinct_prev_prev
    memoization[1] = num_distinct_prev
    memoization[2] = num_distinct
    number += 1


