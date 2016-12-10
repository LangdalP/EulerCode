def sumsquares(num):
	sum = 0
	for i in range(1,num+1):
		sum = sum + i ** 2
	return sum

def squaresum(num):
	square = 0
	for i in range(1,num+1):
		square = square + i
	return square ** 2

n = 100
print(squaresum(n)-sumsquares(n))