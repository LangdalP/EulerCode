from bigint import BigInteger

number = BigInteger("2")
two = BigInteger("2")
for i in range(2, 1001):
    number = number.multiply(two)

digit_sum = 0
for i in range(len(number)):
    digit_sum += number.nth_digit_lsd(i)

print(digit_sum)

