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

prime_sum_limit = 1000000
primes = gen_all_primes_upto(prime_sum_limit + 1)

## Format: (start_idx, len, result)
longest_found = (0, 0, 0)

# For all primes (found by sieve), sum up higher primes until result is not above 1000000
# Note also the index of the last prime that gave a result that was also a prime
for start_idx in range(len(primes)):
    result = primes[start_idx]
    end_idx, prime_end_idx = start_idx + 1, start_idx + 1
    prime_result = result
    while end_idx < len(primes) and result  + primes[end_idx] < prime_sum_limit:
        result += primes[end_idx]
        end_idx += 1
        if result in primes:
            prime_end_idx = end_idx - 1
            prime_result = result
    if (prime_end_idx - start_idx + 1) > longest_found[1]:
        longest_found = (start_idx, prime_end_idx - start_idx + 1, prime_result)

print(longest_found)
