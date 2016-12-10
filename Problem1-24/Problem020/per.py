
num = 100
prod = 1

for i in range(1, num+1):
	prod *= i
print (sum(int(i) for i in str(prod) ))

from math import factorial
print(sum( [ int(i) for i in str(factorial(num)) ] ))
