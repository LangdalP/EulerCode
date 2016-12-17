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

def is_circular(prime, all_primes):
    num_string = str(prime)
    rotations = [num_string[i:] + num_string[:i] for i in range(len(num_string))]
    for rotation in rotations:
        if int(rotation) not in all_primes:
            return False
    return True

all_primes = set(gen_all_primes_upto(1000000))
all_circular_primes = filter(lambda x: is_circular(x, all_primes), all_primes)
print(all_circular_primes)
print(len(all_circular_primes))

