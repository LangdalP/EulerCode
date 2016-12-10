with open("input.txt", "r") as f:
    content = f.read()
names = content.split(",")
names = list(s.strip("\"") for s in names)

names.sort()
totalScore = 0

for i in range(0, len(names)):
	score = 0
	for char in names[i]:
		score += ord(char) - 64
	totalScore += score*(i+1)

print(totalScore)