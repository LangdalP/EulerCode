
def is_together_pandigital(num_list, n):
    digits = set()
    for number in num_list:
        num_string = str(number)
        for digit in num_string:
            digit_num = int(digit)
            if digit_num in digits or digit_num > n or digit_num < 1:
                return False
            digits.add(digit_num)
    return len(digits) == n

candidates = []
for i in range(1, 12000):
    products = []
    num_digits = 0
    for j in range(1, 10):
        product = i * j
        if len(str(product)) + num_digits > 9:
            break
        products.append(product)
        num_digits += len(str(product))
    if num_digits < 10 and is_together_pandigital(products, num_digits):
        pandigital = reduce(lambda x, y: str(x) + str(y), products)
        print("{} x {} gives {}. # digits: {}".format(i, products, pandigital, num_digits))
        candidates.append(int(pandigital))

print(max(candidates))


