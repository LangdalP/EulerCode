
def find_num_right_traingles_with_perimeter(perimeter):
    solution_count = 0
    for a in range(1, perimeter / 3):
        b = a + 1
        while b + a < perimeter:
            c = perimeter - a - b
            if a**2 + b**2 == c**2:
                solution_count += 1
            b += 1
    return solution_count

perimeters = range(10, 1001)
triangles = map(find_num_right_traingles_with_perimeter, perimeters)
best_solution = max(triangles)
best_perimeter = perimeters[triangles.index(best_solution)]
print("Best solution found for perimeter {} with {} triangles".format(best_perimeter, best_solution))
