from math import sqrt
from time import time

"""
------------------------------
SOLUTION 1 - vanskeleg, treig
------------------------------
Problem: Overflow, for store tall
"""

init = time()

digits = 10 ** 999
inPow = 10**5
phi = int((1 + sqrt(5) ) * inPow) // 2

n = 1
f = 0
while f < digits:
	n += 1
	f = ((phi ** n) // (int(sqrt(5)*inPow) * inPow**n / inPow))

print n
print"--- TIME:", time()-init, "---"


"""
------------------------------
SOLUTION 2 - superenkel, rask
------------------------------
"""

init = time()
f = 0
a = 0
b = 1
index = 0
while len(str(a)) < 1000:
	a, b = a+b, a
	index += 1

print index
print"--- TIME:", time()-init, "---"