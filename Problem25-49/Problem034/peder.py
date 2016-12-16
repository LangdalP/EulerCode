from math import factorial
UPPER_TEST_LIMIT = 99999

curious_numbers = []
for i in range(10, UPPER_TEST_LIMIT):
    digit_fac_sum = 0
    for digit in str(i):
        digit_fac_sum += factorial(int(digit))
    if digit_fac_sum == i:
        curious_numbers.append(i)

print(curious_numbers)
print(sum(curious_numbers))

