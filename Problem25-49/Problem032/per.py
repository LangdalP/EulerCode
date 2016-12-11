def iGen(n):
	for i in range(2, n):
		dig = set()
		for digit in repr(i):
			dig.add(digit)
		if len(dig) == len(str(i)):
			yield i

def kGen(n, prev):
	for i in range(2, n):
		dig = set()
		for digit in repr(i):
			dig.add(digit)
		for digit in repr(prev):
			dig.add(digit)
		if len(dig) == len(str(i)) + len(str(prev)):
			yield i

def isPandigital(i, k, p):
	string = str(p)+str(i)+str(k)
	if len(string) != 9:
		return 0
	for char in range(0, len(string)):
		for char2 in range(char + 1, len(string)):
			if string[char] == string[char2]:
				return 0
			elif string[char] == "0":
				return 0
	return p	

pandigitalProduct = set()
notPandigital = set()

for i in iGen(10000):
	for k in kGen(10000, i):
		p = i * k
		if isPandigital(i, k, p):
			pandigitalProduct.add(p)
print "p", sorted(pandigitalProduct)
print sum(pandigitalProduct)