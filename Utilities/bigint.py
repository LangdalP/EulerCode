
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

    def nth_digit_msd(self, n):
        # The most significant digit is the 0-th digit
        if n >= len(self.value):
            return None
        return int(self.value[n])

    def num_digits(self):
        return len(self.value)

    def compare(self, other):
        # 1 means self is largest, 0 means equal numbers, -1 means other is largest
        if len(self) > len(other):
            return 1
        if len(other) > len(self):
            return -1
        if str(self) == str(other):
            return 0
        for i in range(0, len(self)):
            self_digit = self.nth_digit_msd(i)
            other_digit = other.nth_digit_msd(i)
            if self_digit > other_digit:
                return 1
            if self_digit < other_digit:
                return -1
        return 0

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

    def multiply(self, other):
        my_length = self.num_digits()
        other_length = other.num_digits()
        longest_factor = max(my_length, other_length)
        subsums = []
        if my_length >= other_length:
            upper_number = self
            lower_number = other
        else:
            upper_number = other
            lower_number = self
        # print("Starting mult. Up: {} Low {}".format(upper_number, lower_number))
        # First multiplication step
        for i in range(len(lower_number)):
            carry = 0
            subsum_string = ""
            for j in range(len(upper_number)):
                up_digit = upper_number.nth_digit_lsd(j)
                lo_digit = lower_number.nth_digit_lsd(i)
                multiplied = up_digit * lo_digit + carry
                carry = 0
                # print("Upd: {} Lod: {} Mult: {}".format(up_digit, lo_digit, multiplied))
                while multiplied >= 10:
                    carry += 1
                    multiplied -= 10
                # print("Adding {} to subsum".format(multiplied))
                subsum_string += str(multiplied)
            if carry > 0:
                subsum_string += str(carry)
            subsum_string = subsum_string[::-1]
            for i in range(i):
                subsum_string += "0"
            subsums.append(subsum_string)
        # Second addition part
        sum = BigInteger("0")
        for subsum in subsums:
            subsum_bigint = BigInteger(subsum)
            sum = sum.add(subsum_bigint)
        return sum

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return str(self.value)

if __name__ == "__main__":
    num1 = BigInteger("469")
    num2 = BigInteger("32")
    print(num1.multiply(num2))
    num3 = BigInteger("5127")
    num4 = BigInteger("4265")
    print(num3.multiply(num4))

