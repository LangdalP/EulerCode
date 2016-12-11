from math import sqrt

def find_factors(n):
    factors = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)   # Factors come in pairs
    return factors

def find_amicable_numbers_below(below_limit):
    # First find all factor sums
    factor_sums = [sum(find_factors(i)) for i in range(2, below_limit * 2)]
    # Then find if any are amicable
    amicable_numbers = []
    for i in range(0, len(factor_sums)):
        current_number = i + 2
        current_factor_sum = factor_sums[i]
        # Check overflow, underflow, uniqueness, and amicability
        if (current_factor_sum != 1 and
                current_factor_sum < len(factor_sums) + 1 and
                factor_sums[current_factor_sum - 2] == current_number and
                current_number < current_factor_sum):
            amicable_numbers.extend([current_number, current_factor_sum])
    return filter(lambda x: True if x < below_limit else False,
            amicable_numbers)

if __name__ == "__main__":
    amicable_numbers = find_amicable_numbers_below(10000)

    print(amicable_numbers)
    print(sum(amicable_numbers))

