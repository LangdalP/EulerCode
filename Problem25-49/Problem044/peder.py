
def penta_gen(from_n, to_n):
    for n in range(from_n, to_n):
        yield n * (3*n -1)/2

penta_list = list(penta_gen(1, 10000))
penta_set = set(penta_list)

candidates = []
for i in range(0, len(penta_list)):
    num1 = penta_list[i]
    for j in range(i, len(penta_list)):
        num2 = penta_list[j]
        sum = num1 + num2
        difference = abs(num1 - num2)
        if sum in penta_set and difference in penta_set:
            candidates.append((num1, num2))

print(candidates)
# Only 1 candidate with upper-limit = 10000
print(candidates[0][1] - candidates[0][0])

