fib = 2
total = 2
last = 1

while fib < 4000000:
	lasttmp = fib
	fib = fib + last
	last = lasttmp
	if fib % 2 == 0:
		total = total + fib
	print("Fib: ", fib, "  Total: ", total)
print(total)