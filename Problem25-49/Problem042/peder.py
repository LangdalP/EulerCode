
most_triangle_numbers = set(map(lambda x: (x*(x + 1))/2, range(1, 100)))
with open("input.txt") as f:
    words = f.read().replace("\"", "").split(",")

num_triangle_words = 0
for word in words:
    word_value = sum(map(lambda letter: (ord(letter) - ord('A') + 1), word))
    if word_value in most_triangle_numbers:
        num_triangle_words += 1

print(num_triangle_words)

