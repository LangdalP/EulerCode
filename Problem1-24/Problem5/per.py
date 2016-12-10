num = 20
edivide = False
while not edivide:
	num += 20
	for i in range(2,21):
		if num % i != 0:
			edivide = False
			break
		else:
			edivide = True
	if num > 1000000000:
		break

if edivide:
	print("SUCCESS!")
print(num)