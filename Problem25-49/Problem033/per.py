import fractions
def numGen():
	for i in range(10, 100):
		if i % 10 != 0:
			yield i
product1, product2 = 1, 1
for i in numGen():
	for k in numGen():
		if i != k:
			num1, num2 = str(i), str(k)
			if float(num1[0]) / float(num2[1]) == float(num1) / float(num2):
				if num1[0] != num1[1] and num2[0] != num2[1]:
					if num1[1] == num2[0]:
						product1 *= float(i)
						product2 *= float(k)
						print product1, product2

print(product2 / fractions.gcd(product1, product2))