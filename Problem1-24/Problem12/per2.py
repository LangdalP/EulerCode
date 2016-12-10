i = 0
while True:
    d, n = 2, sum(range(i))
    print(int(n ** 0.5), n)
    for x in range(2, int(n ** 0.5)):
        if not n % x:
            d += 2
    if d > 3: break
    i += 1
print(n)