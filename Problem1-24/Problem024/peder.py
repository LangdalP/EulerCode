from math import factorial

def create_all_permutations(digits):
    if len(digits) == 1:
        return [str(digits[0])]
    permutations = []
    for i in range(0, len(digits)):
        starting_digit = digits[i]
        other_digits = [x for x in digits if x != starting_digit]
        remaining_permutations = create_all_permutations(other_digits)
        for i in range(0, len(remaining_permutations)):
            remaining_permutations[i] = str(starting_digit) + remaining_permutations[i]
        permutations.extend(remaining_permutations)
    return permutations

# Set first digit, calculate possible permutations from the remaining digits.
# A counter keeps track of how many permutations we have gone through.
# When it goes above n, we either do a recursive call or calculate all
# permutations from the remaining digits.
def create_nth_permutation(digits, n):
    counter = 0
    for i in range(0, len(digits)):
        starting_digit = digits[i]
        remaining_permutations = factorial(len(digits) - 1)
        if counter + remaining_permutations > n - 1:
            print(i)
            # How much further until we are close?
            difference = n - counter
            if len(digits) > 5:
                other_digits = [x for x in digits if x != starting_digit]
                return str(starting_digit) + create_nth_permutation(other_digits, difference)
            else:
                perms = create_all_permutations(digits)
                return perms[counter + difference]
        else:
            counter += remaining_permutations

if __name__ == "__main__":
    nth = create_nth_permutation([0,1,2,3,4,5,6,7,8,9], 999999)
    print(nth)

