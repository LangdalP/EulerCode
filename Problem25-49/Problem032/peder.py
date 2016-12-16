
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

pan_products = []
for i in range(1, 9999):
    for j in range(i, 9999):
        product = i * j
        if is_together_pandigital([i, j, product], 9):
            print("{} x {} = {}".format(i, j, product))
            pan_products.append(product)
        if len(str(i) + str(j) + str(product)) > 9:
            break

print(sum(set(pan_products)))

