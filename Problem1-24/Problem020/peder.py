
def fac(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def digit_sum(n):
    digit_string = str(n)
    result = 0
    for digit in digit_string:
        value = int(digit)
        result += value
    return result

if __name__ == "__main__":
    number = fac(int(100))
    print(number)
    dig_sum = digit_sum(number)
    print(dig_sum)

