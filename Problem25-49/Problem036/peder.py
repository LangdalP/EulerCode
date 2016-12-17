
def is_palindrome(num_string):
    length = len(num_string)
    for i in range(length/2 + 1):
        if num_string[i] != num_string[length - 1 - i]:
            return False
    return True

sum = 0
for i in range(1000000):
    binary_string = "{0:b}".format(i)
    if is_palindrome(str(i)) and is_palindrome(binary_string):
        print(i)
        sum += i

print("Sum: {}".format(sum))

