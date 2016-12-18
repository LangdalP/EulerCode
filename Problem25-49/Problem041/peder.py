from math import sqrt

def is_pandigital(number):
    digits = set()
    num_string = str(number)
    n = len(num_string)
    for digit in num_string:
        digit_num = int(digit)
        if digit_num in digits or digit_num > n or digit_num < 1:
            return False
        digits.add(digit_num)
    return len(digits) == n

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

all_primes = gen_all_primes_upto(10000000)
pandigital_primes = filter(lambda x: is_pandigital(x), all_primes)
print(pandigital_primes)
print(max(pandigital_primes))
