sumDiagonals = 1
shell = 1
prevHigh = 1

while shell*2-1 < 1001:
	shell += 1
	outer = []
	for i in range(prevHigh + 1, prevHigh + (shell*2-2) * 4 + 1):
		outer.append(i)
	for k in range(1,5):
		sumDiagonals += outer[k*(shell*2-2)-1]

	prevHigh = i

print sumDiagonals