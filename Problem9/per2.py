"""
s = 1000
for a in range(3, int((s-3)/3)):
	for b in range(a+1, int((s-1-a)/2)):
		c = s-b-a
		if c*c == a*a + b*b:
			print(a, b, c)
"""
import math
#fungera opp til 10^10 jævli fort
s1 = 213123213213
s2 = s1//2
mlimit = int(math.sqrt(s2))-1
for m in range(2, mlimit):
	if s2 % m == 0:
		sm = s2 // m
		while sm % 2 == 0:
			sm = sm // 2
		if m % 2 == 1:
			k = m+2
		else:
			k = m+1
		while k < 2*m and k <= sm:
			if sm % k == 0 and math.gcd(k,m) == 1:
				d = s2 // (k*m)
				n = k-m
				a = d*(m*m-n*n)
				b = 2*d*m*n
				c = d*(m*m+n*n)
				print (a, b, c, "sum abc:", a+b+c)
			k = k + 2