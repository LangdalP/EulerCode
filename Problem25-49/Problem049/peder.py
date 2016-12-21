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

# Generate all 4-digit numbers in sequence, check if they are all prime and contain the same digits
def find_arithmetic_progression_and_check_if_satifies(num1, num2):
    d = abs(num1 - num2)
    lowest = min(num1, num2)
    highest = max(num1, num2)
    progression_members = [lowest, highest]
    # Complete sequence in range (1000, 10000)
    while lowest - d > 1000:
        new_lowest = lowest - d
        lowest = new_lowest
        progression_members.append(new_lowest)
    while highest + d < 10000:
        new_highest = highest + d
        highest = new_highest
        progression_members.append(new_highest)
    if len(progression_members) != 3:
        return False
    allowed_digits = set(str(num1))
    for member in progression_members:
        member_digits = set(str(member))
        if member_digits != allowed_digits or member not in primes:
            return False
    return progression_members

# Primes between 1000 and 10 000
primes = set(filter(lambda x: x > 1000, gen_all_primes_upto(10000)))

# Problem was not clear on whether the difference was infact 3330, but it was
# Initially I had a second for-loop below where d ranged from 2500 to 3800
d = 3330

for prime in primes:
    result = find_arithmetic_progression_and_check_if_satifies(prime, prime + d)
    if result:
        print(result)

