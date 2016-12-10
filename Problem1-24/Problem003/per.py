"""
prime = []
found = False
number = 600851475143 

for i in range(2,7000):
	for j in range(2,i+1):
		if i % j == 0 and i!=j:
			found = True
			break

	if not found:
		prime.append(i)

	found = False

while number > 1:
	for item in prime:
		if number % item  == 0:
			print("Prime:", item)
			number = number / item
			break
"""
import math 
def isprime(n): 
	return not any(n%i == 0 for i in range (2,n)) 

input=600851475143 
max=input 
prime = []
tmp = 1

for i in range(2, int(math.sqrt(max))): 
	if input %i==0: 
		if isprime(i): 
			max=i 
			prime.append(i)
			tmp = 1
			for item in prime:
				tmp = tmp * item

			if tmp == input:
				break
print(max)