def getDivisorSum(n):
	divSum = 1
	for i in range(2, n//2 + 1):
		if n % i == 0:
			divSum += i
	return divSum

d = [[1]]
am = []
dub = []
for i in range(1, 10000):
	d.append([i])
	d[i].append(getDivisorSum(i))

for a in range(1, 10000):
	if d[a][1] < 10000:
		if a == d[d[a][1]][1] and a != d[d[a][1]][0]:
			print(a, d[a][0], d[a][1], d[d[a][1]][0], d[d[a][1]][1])
			am.append(a)
print(am)
print(sum(am))