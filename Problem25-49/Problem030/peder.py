POWER = 5

numbers_found = []
for i in range(10, 1000000):
    num_string = str(i)
    power_sum = 0
    for digit in num_string:
        power_sum += int(digit)**POWER
    if power_sum == i:
        numbers_found.append(i)

print(numbers_found)
print(sum(numbers_found))

