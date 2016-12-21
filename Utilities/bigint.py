
class BigInteger:
    '''
    Class for simple big integer (> 64 bits) operations
    Internally uses a base-10 string representation
    Python's 'long' type is the preferred way to do such operations.
    This class is simply made to learn how BigIntegers can be implemented.
    '''

    def __init__(self, init_value=0):
        # TODO: Remove these tests if the same is done in all vases
        if type(init_value) is int or type(init_value) is float or type(init_value) is str:
            self.value = str(init_value)
        else:
            self.value = None
            raise ValueError('Invalid initial value!')

    def nth_digit_lsd(self, n):
        # The least significant digit is the 0-th digit
        if n >= len(self.value):
            return None
        return int(self.value[-1 - n])

    def num_digits(self):
        return len(self.value)

    def add(self, other):
        my_length = self.num_digits()
        other_length = other.num_digits()
        longest_addend = max(my_length, other_length)
        digits = ""
        carry = 0
        for i in range(0, longest_addend):
            my_digit = self.nth_digit_lsd(i) if i < my_length else 0
            others_digit = other.nth_digit_lsd(i) if i < other_length else 0
            digits_added = my_digit + others_digit + carry
            if digits_added >= 10:
                digits_added -= 10
                carry = 1
            else:
                carry = 0
            digits = digits + str(digits_added)
        if carry == 1:
            digits = digits + str(1)
        digits_reversed = digits[::-1]
        return BigInteger(digits_reversed)

    def __repr__(self):
        return str(self.value)

if __name__ == "__main__":
    # Just some basic testing
    num1 = BigInteger("1")
    num2 = BigInteger("99999999999999999999999999999999999999999999999999999999")
    num3 = num1.add(num2)
    print(num2.num_digits())
    print(num3.num_digits())
    print(num3)

