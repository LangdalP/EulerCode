
# n^2 + an + b
# -1000 < a < 1000  and  -1000 <= b <= 1000

PRIME_CHECK_LIMIT = 1000

def is_prime_naive(number):
    if number < 2:
        return False
    for i in range(2, int(number/2) + 1):
        if number % i== 0:
            return False
    return True

def check_consecutive_primes(a,b):
    consecutive_found = 0
    for n in range(0, PRIME_CHECK_LIMIT):
        potential_prime = n**2 + a*n + b
        if is_prime_naive(potential_prime):
            consecutive_found += 1
        else:
            return consecutive_found

def test_all_quadratics():
    highest_consecutive = 0
    highest_ab = (None, None)
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            consecutive = check_consecutive_primes(a,b)
            if consecutive > highest_consecutive:
                highest_consecutive = consecutive
                highest_ab = (a, b)
    return highest_consecutive, highest_ab[0], highest_ab[1]

result = test_all_quadratics()
print(result)

