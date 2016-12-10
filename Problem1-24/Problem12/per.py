triSum = 0
triNum = 1
numdivides = 500
test = []

while True:
	divide = 1
	useless = 0
	lastProd = 0

	triSum += triNum
	if triSum % 2 == 0 and triSum % 3 == 0:
		for j in range(2, triSum//2+1):
			if triSum % j == 0:
				if lastProd == j:
					divide = divide * 2
					#print("hallo", divide, lastProd, triSum, triNum)
					break
				divide += 1
				lastProd = triSum // j

	if divide > numdivides:
		test.append(1)
		for j in range(2, triSum//2+1):
			if triSum % j == 0:
				test.append(j)
		
		print("SUCCESS!")
		print("Triangle:", triSum, "Dividers:", divide, "Trinangle nr:", triNum)
		#print(test)
		break
		
	triNum += 1