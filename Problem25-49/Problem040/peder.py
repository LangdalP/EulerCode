
# Just loop over all integers from 1 until we find nth digit
# Increment digit counter as numbers as passed by
def find_these_digits(digit_list):
    num_digits_remaining = len(digit_list)
    digit_counter = 1
    integer_counter = 1
    found_digits = []
    while num_digits_remaining > 0:
        digits = str(integer_counter)
        if digit_list[0] < digit_counter + len(digits):
            found_digits.append(int(digits[digit_list[0] - digit_counter]))
            del digit_list[0]
            num_digits_remaining -= 1
        integer_counter += 1
        digit_counter += len(digits)
    return found_digits

digits = find_these_digits([1, 10, 100, 1000, 10000, 100000, 1000000])
digits_multiplied = reduce(lambda x, y: x*y, digits)
print(digits)
print(digits_multiplied)
