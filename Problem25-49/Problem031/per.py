coins = [1, 2, 5, 10, 20, 50, 100, 200]
twoPounds = 200
comb = 0

def numCombinations(nums, startNum, n):
	if n == 0:
		return
	elif startNum == 0:
		global comb
		comb += 1
		return
	elif startNum < 0:
		return
	
	for i in range(len(nums)):
		if startNum - nums[i] >= 0:
			numCombinations(nums[i:len(nums)], startNum - nums[i], n-1)
		else:
			break
	return


numCombinations(coins, twoPounds, twoPounds+1)
print comb