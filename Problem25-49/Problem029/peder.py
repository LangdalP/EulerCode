
unique_numbers = set()
for a in range(2, 101):
    for b in range(2, 101):
        unique_numbers.add(a**b)
print(len(unique_numbers))

