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

def is_truncatable(prime, all_primes):
    if prime < 10:
        return False
    num_string, length = str(prime), len(str(prime))
    for i in range(1, length):
        truncated_l_to_r = int(num_string[i:])
        truncated_r_to_l = int(num_string[:length - i])
        if truncated_l_to_r not in all_primes or truncated_r_to_l not in all_primes:
            return False
    return True

all_primes = gen_all_primes_upto(1000000)
truncatable_primes = filter(lambda x: is_truncatable(x, all_primes), all_primes)
truncatable_sum = sum(truncatable_primes)

print(truncatable_primes)
print(truncatable_sum)
