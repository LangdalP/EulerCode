# TODO: Burde prøve å lage eigen "BigInteger"-type

if __name__ == "__main__":
    num1 = 1
    num2 = 1
    index = 2
    while len(str(num2)) < 1000:
        next = num1 + num2
        index += 1
        num1, num2 = num2, next
    print(index)
    print(num2)

