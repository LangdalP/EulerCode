def ispyth(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	return False

def isthousand(a,b,c):
	return a+b+c

found = False
for a in range(1,1000):
	for b in range(a+1,1000):
		for c in range(b+1,1000):
			sum = isthousand(a,b,c)
			if sum == 1000:
				if ispyth(a,b,c):
					print("SUCCESS: ", a,b,c, "Product: ", a*b*c)
					found = True
					break
			elif sum > 1000:
				break
		if found:
			break
	if found:
		break

