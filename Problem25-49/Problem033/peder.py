
def can_cancel_digits(a, b):
    value = (1.0*a)/b
    a_str, b_str = str(a), str(b)
    if a_str[1] == b_str[0]:
        new_a, new_b = int(a_str[:1]), int(b_str[1:])
        if new_b == 0:
            return False
        if (1.0*new_a)/new_b == value:
            return True
    return False

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

product_numerator = 1
product_denominator = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        if can_cancel_digits(i, j):
            product_numerator *= i
            product_denominator *= j
            print("{} / {}".format(i,j))

# Simplify fraction
num_denom_gcd = gcd(product_numerator, product_denominator)
print(product_denominator/num_denom_gcd)

