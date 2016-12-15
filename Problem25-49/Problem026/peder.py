from decimal import *

def find_reciprocal_cycle(d, precision):
    getcontext().prec = precision # Decimal precision
    longest_period = 0
    longest_reciprocal = (None, None, None)
    for i in range(2, d):
        decimal_string = str(Decimal(1.0) / Decimal(i))
        fraction_part = decimal_string.split(".")[1]
        for repeating_start in range(0, 10):
            for cycle_period in range(1, int(precision/2)):
                potential_reciprocal = fraction_part[repeating_start:repeating_start + cycle_period]
                # Check if next substring of same length is the same
                next_substring = fraction_part[repeating_start + cycle_period:repeating_start + 2 * cycle_period]
                if next_substring == potential_reciprocal:
                    if cycle_period > longest_period:
                        longest_period = cycle_period
                        longest_reciprocal = (i, decimal_string, potential_reciprocal)
                    break
    return longest_period, longest_reciprocal

if __name__ == "__main__":
    period, number_info = find_reciprocal_cycle(1000, precision=2000)
    print("d = {} gives period {}. ({})".format(number_info[0], period, number_info[1]))


