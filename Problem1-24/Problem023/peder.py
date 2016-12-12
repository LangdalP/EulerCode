# Perfect num: Sum of its proper divisors is exactly equal to the number
# Deficient num: sum < num
# Abundant num: sum > num

# Abundant ex.: 12. 1+2+3+4+6 = 16
# Smallest number that is the sum of two abundant numbers is 24

# All ints > 28123 can be written as the sum of two abundant numbers
# (But also some other ints below this limit can be written as sum

# Find the sum of all the positive ints that cannot be written as sum of two ab. nums

from math import sqrt

def find_factors(n):
    factors = [1]
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)   # Factors come in pairs

    # A perfect square will give one duplicate factor
    is_perfect_square = n == int(sqrt(n)) * int(sqrt(n))
    if is_perfect_square:
        factors = factors[:-1]
    return factors

def generate_all_abundants_below(upper_limit):
    abundants = set()
    for i in range(12, upper_limit + 1):
        factor_sum = sum(find_factors(i))
        if factor_sum > i:
            abundants.add(i)
    return abundants

def generate_all_addition_combinations(addends):
    addends_list = list(addends)
    results = []
    for i in range(0, len(addends_list)):
        for j in range(i, len(addends_list)):
            results.append(addends_list[i] + addends_list[j])
    return set(results)

if __name__ == "__main__":
    abundants = generate_all_abundants_below(28124)
    combinations = generate_all_addition_combinations(abundants)
    sum = 0
    for i in range(1, 28124):
        if i not in combinations:
            sum += i
    print(sum)

