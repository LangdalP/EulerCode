from langint import LangInteger

number = LangInteger("2")
two = LangInteger("2")
for i in range(2, 1001):
    number = number.multiply(two)

digit_sum = 0
for i in range(len(number)):
    digit_sum += number.nth_digit_lsd(i)

print(digit_sum)

