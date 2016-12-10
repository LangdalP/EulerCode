grid = [20,20]
routes = 0

def bio(n, k):
	over = 1
	under = 1
	for i in range(n, n-k, -1):
		over *= i
	for i in range(2, k + 1):
		under *= i
	return over//under

print(bio(max(grid)+min(grid), min(grid)))