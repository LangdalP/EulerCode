from math import sin, cos, pi

# Start on (x,y), go in direction (dx, dy) until border
def sum_direction(grid, x, y, dx, dy):
    diag_sum = grid[y][x]
    while True:
        diag_sum += grid[y + dy][x + dx]
        x, y = x + dx, y + dy
        if y + dy >= len(grid) or x + dx >= len(grid[0]):
            break
    return diag_sum

ANGLE = pi/2
def next_dir(dx, dy):
    new_dx = int(dx*cos(ANGLE) - dy*sin(ANGLE))
    new_dy = int(dx*sin(ANGLE) + dy*cos(ANGLE))
    return (new_dx, new_dy)

# For each iteration: set value, then set new direction and new position
def spiral_walk(grid):
    middle_coord = side_length // 2
    counter = 1
    x, y = middle_coord, middle_coord
    dx, dy = 0, -1
    while True:
        grid[y][x] = counter
        counter += 1
        new_dx, new_dy = next_dir(dx, dy)
        if grid[y + new_dy][x + new_dx] == 0:       # Can I turn clockwise?
            dx, dy = new_dx, new_dy
        x, y = x + dx, y + dy
        if y >= len(grid) or x >= len(grid[0]):
            return

side_length = 1001
grid = [[0 for x in range(side_length)] for y in range(side_length)] 
spiral_walk(grid)
diagonals = sum_direction(grid, 0, 0, 1, 1) + sum_direction(grid, 0, side_length - 1, 1, -1) - 1
print(diagonals)

# def print_grid(grid):
    # for i in range(0, len(grid)):
        # line_string = ""
        # for j in range(0, len(grid[0])):
            # line_string += "{:03d}".format(grid[i][j]) + " "
        # print(line_string)
