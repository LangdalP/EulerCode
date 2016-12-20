from math import sqrt

# For a given triangular number, solve equations for
# pentagonal and hexagonal numbers for n, and see if 
# n is a whole number (integer). If it seems like a
# whole number, calculate the pentagonal and hexagonal
# number and see if they are equal

coefficient_map = {
        'tri': lambda y: (1, 1, -2*y),
        'penta': lambda y: (3, -1, -2*y),
        'hexa': lambda y: (2, -1, -y)
}

number_calc_map = {
        'tri': lambda n: n*(n + 1)/2,
        'penta': lambda n: n*(3*n - 1)/2,
        'hexa': lambda n: n*(2*n - 1)
}

def solve_poly_2(a, b, c):
    sqrt_part = sqrt(b**2 - 4*a*c)
    x1 = (-b + sqrt_part)/(2*a)
    x2 = (-b - sqrt_part)/(2*a)
    return (x1, x2)

def find_n(num_type, number):
    coefficients = coefficient_map[num_type](number)
    solutions = solve_poly_2(*coefficients)
    return max(solutions)

def is_close_to_integer(number):
    closest_int = round(number)
    if number < closest_int + 0.0001 and number > closest_int - 0.0001:
        return True
    return False

n_tri = 286
while True:
    triangular = number_calc_map['tri'](n_tri)
    n_penta = find_n('penta', triangular)
    n_hexa = find_n('hexa', triangular)
    if is_close_to_integer(n_penta) and is_close_to_integer(n_hexa):
        pentagonal = number_calc_map['penta'](int(n_penta))
        hexagonal = number_calc_map['hexa'](int(n_hexa))
        print("n_tri = {}, triangular = {}, pentagonal = {}, hexagonal = {}".format(n_tri, triangular, pentagonal, hexagonal))
        if triangular == pentagonal and triangular == hexagonal:
            print("Found solution!")
            break
    n_tri += 1

