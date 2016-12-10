with open("input.txt", "r") as f:
    content = f.read()
names = content.split(",")
names = list(s.strip("\"") for s in names)
print(names[:10])