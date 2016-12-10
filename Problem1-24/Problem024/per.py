from time import time
init_time = time()
numbers = [0,1,2,3,4,5,6,7,8,9]
reverse = []
numPerm = 1

for b in range(1,10**6):
	found = False
	for i in range(len(numbers)-2, -1, -1):
		if numbers[i] < numbers[i+1]:

			for l in range(len(numbers)-1, i, -1):
				if numbers[l] > numbers[i]:
					numbers[i], numbers[l] = numbers[l], numbers[i]
					reverse = numbers[0:i+1]
					reverse[i+1:len(numbers)] = numbers[i+1:len(numbers)][::-1]
					numbers = reverse
					found = True
					numPerm += 1
					break
		if found == True:
			break

print (numbers)
print (time()-init_time)