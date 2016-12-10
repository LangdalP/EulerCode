def calc(n):
	chain = 1
	while n != 1:
		if n % 2 == 0:
			n //= 2
		else:
			n = n * 3 + 1
		chain += 1
	return chain


hiStart = 0
hiChain = 0

for start in range(1,10**6, 2):
	chain = calc(start)

	if chain > hiChain:
		hiStart	= start
		hiChain = chain

print(hiStart)
print(hiChain)