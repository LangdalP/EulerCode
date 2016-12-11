

distinctPowers = set()

for a in range(2, 101):
	for b in range(2, 101):
		distinctPowers.add(a**b)

print len(sorted(distinctPowers))