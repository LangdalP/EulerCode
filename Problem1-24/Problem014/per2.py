m, p = 0, 0
for i in range(1, 1000000, 2):
    count, pos = 1, i
    while i != 1:
        if not i % 2:
            i //= 2
        else:
            i += i + i + 1
        count += 1
    if count > m:
        m, p = count, pos
print('count %d position %d'%(m, p))