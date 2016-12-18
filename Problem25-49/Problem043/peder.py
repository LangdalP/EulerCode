
DIVISIBLE_BY = [2,3,5,7,11,13,17]
DIGITS = [(1,2,3), (2,3,4), (3,4,5), (4,5,6), (5,6,7), (6,7,8), (7,8,9)]

def has_divisibility_property(number):
    num_string = str(number)
    for j in range(0, len(DIVISIBLE_BY)):
        a, b, c = DIGITS[j]
        divisible_by = DIVISIBLE_BY[j]
        digits = num_string[a] + num_string[b] + num_string[c]
        if not int(digits) % divisible_by == 0:
            return False
    return True

def find_largest_pairwise(func, collection):
    for i in range(len(collection) - 1, 0, -1):
        good_pair = func(collection[i - 1], collection[i])
        if good_pair:
            return i - 1, i
    return None

def find_largest_single(func, collection):
    for i in range(len(collection) - 1, -1, -1):
        good_item = func(collection[i])
        if good_item:
            return i
    return None

# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
def create_all_digit_permutations(num_digits):
    digits = range(0, num_digits)
    permutations = [reduce(lambda x, y: str(x) + str(y), digits)]
    while True:
        k = find_largest_pairwise(lambda x, y: x < y, digits)
        if not k:
            return permutations
        else:
            k = k[0]
        l = find_largest_single(lambda x: x > digits[k], digits)
        digits[l], digits[k] = digits[k], digits[l]     # Swap l and k
        end_part = digits[k+1:]
        digits[k+1:] = end_part[::-1]                   # Reverse everything after k + 1
        permutations.append(reduce(lambda x, y: str(x) + str(y), digits))
    return permutations

all_permutations = set(map(lambda x: int(x), create_all_digit_permutations(10)))
all_candidates = filter(lambda x: x > 1000000000, all_permutations)
all_divisible_permutations = filter(has_divisibility_property, all_candidates)
print(sum(all_divisible_permutations))

