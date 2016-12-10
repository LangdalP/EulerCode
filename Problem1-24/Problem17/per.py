ten = ["one", "two", "three", "four", "five", "six", "seven", "eigth", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
two = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
a = "and"
h = "hundred"
numChar = 0


for i in range(1, 1001):
	numString = ""
	
	if i < 20:
		numString += ten[i-1]

	elif 19 < i < 100:
		numString += two[i//10-2]
		if i % 10 != 0:
			numString += ten[i%10-1]

	elif 99 < i < 1000:
		numString += ten[i // 100 - 1] + h
		if i % 100 != 0:
			numString += a
			if i % 100 < 20:
				numString += ten[i%100-1]
			elif i % 100 > 19:
				numString += two[(i // 10) % 10-2]
				if i % 10 != 0:
					numString += ten[i%10-1]

	elif i == 1000:
		numString = "onethousand"

	numChar += len(numString)
	print(i, numString, len(numString), numChar)
print(numChar)