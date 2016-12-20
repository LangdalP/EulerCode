
# Lets just see if Python can handle it
# NB: This is obviously another "BigInteger" test
# TODO: Implement own BigInteger
sum = 0
for i in range(1, 1001):
    sum += i**i

print(str(sum)[-10:])

