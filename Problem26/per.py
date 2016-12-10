from decimal import *

dMax = 1000
getcontext().prec = 5000
longest = 0

for i in range(2,dMax+1):
	num = str(1/(Decimal(i)))
	num = num.split(".")
	num = num[1]
	while num[0] == "0":
		num = num[1:len(num)]
	
	for n in range(1, len(num)):
		if num[0] == num[1]:
			break
		if num[0:n] == num[n:n*2]:
			if longest < n:
				longest = n
				longestD = i
			break

print i, longest, longestD