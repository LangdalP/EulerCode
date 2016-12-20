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

UPPER_LIMIT = 1000000
many_primes = gen_all_primes_upto(UPPER_LIMIT)
many_primes_set = set(many_primes)

def try_find_square(target_num):
    primes_to_try = filter(lambda x: x < target_num, many_primes)
    for prime in primes_to_try:
        sum, i = 0, 0
        while sum <= target_num:
            sum = prime + 2*(i**2)
            if sum == target_num:
                return True
            i += 1
    return False

for i in range(11, UPPER_LIMIT, 2):
    if i in many_primes:
        continue
    if try_find_square(i):
        continue
    else:
        print("Couldn't find sum for the number {}".format(i))
        break

