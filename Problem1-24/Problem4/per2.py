import time
start_time = time.time()

start = 99999
stop = 9999
highestPalin = 0
for first in range(start, stop, -1):
	for second in range(start, stop, -1):
		prod = first*second
		if prod < highestPalin:
			break
		prodstr=str(prod)
		if prodstr == prodstr[::-1]:
			if prod > highestPalin:
				highestPalin = prod
		if prod < highestPalin:
			break
print(highestPalin)

print("--- %.3f seconds ---" % (time.time() - start_time))