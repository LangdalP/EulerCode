def isFiftPowers(n):
	oneNum = str(n)
	total = 0
	for i in range(0, len(oneNum)):
		total += int(oneNum[i]) ** 5
	if total == n:
		return True
	return False



sumFiftPowers = 0

for num in range(2, 10000000):
	if isFiftPowers(num):
		sumFiftPowers += num
		print num

print sumFiftPowers
