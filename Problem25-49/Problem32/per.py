def iGen(n):
	for i in range(2, n):
		dig = set()
		for digit in repr(i):
			dig.add(digit)
		if len(dig) == len(str(i)):
			yield i

def kGen(n, prev):
	for i in range(2, n):
		dig = set()
		for digit in repr(i):
			dig.add(digit)
		for digit in repr(prev):
			dig.add(digit)
		if len(dig) == len(str(i)) + len(str(prev)):
			yield i

def isPandigital(i, k, p):
	string = str(p)+str(i)+str(k)
	if len(string) != 9:
		return 0
	for char in range(0, len(string)):
		for char2 in range(char + 1, len(string)):
			if string[char] == string[char2]:
				return 0
			elif string[char] == "0":
				return 0
	return p	

pandigitalProduct = set()
pandigitalMultiplier = set()
pandigitalMultiplicand = set()
notPandigital = set()
for i in iGen(10000):
	for k in kGen(10000, i):
		p = i * k
		if isPandigital(i, k, p):
			pandigitalProduct.add(p)
			pandigitalMultiplier.add(i)
			pandigitalMultiplicand.add(k)
print "p", sorted(pandigitalProduct)
print "i", pandigitalMultiplier 
print "k", pandigitalMultiplicand
print sum(pandigitalProduct)
"""
test = {3, 4, 5, 7, 8, 9, 15, 17, 18, 19, 34, 35, 38, 39, 43, 45, 48, 53, 54, 65, 
67, 69, 73, 78, 79, 85, 93, 154, 178, 179, 185, 307, 309, 345, 354, 358, 359, 
415, 435, 453, 458, 465, 478, 485, 534, 538, 539, 543, 548, 654, 679, 685, 769, 
793, 835, 845, 853, 865, 935, 1548, 1845, 3079, 3485, 3548, 3845, 4518, 4538, 
4685, 4815, 4835, 4853, 4865, 2, 6, 16, 26, 27, 29, 58, 64, 68, 87, 89, 168, 169, 
176, 182, 189, 192, 194, 218, 219, 267, 269, 568, 582, 594, 609, 658, 819, 906, 
916, 918, 1609, 1694, 1809, 1908, 2058, 5694, 6819, 6918, 8169, 9168, 13, 59, 92, 
95, 127, 152, 157, 158, 173, 195, 209, 215, 259, 392, 517, 519, 579, 695, 709, 
715, 789, 792, 795, 815, 879, 907, 1738, 1963, 2039, 2079, 3907, 7039, 9127, 12, 
14, 28, 32, 36, 46, 62, 72, 76, 82, 86, 96, 128, 134, 138, 146, 164, 172, 184, 
186, 268, 276, 278, 286, 296, 328, 364, 372, 384, 436, 438, 476, 628, 682, 728, 
762, 764, 782, 784, 826, 832, 862, 872, 962, 972, 1278, 1384, 1846, 1864, 1872, 
57, 97, 145, 289, 293, 529, 703, 817, 903, 913, 1309, 5817, 24, 52, 56, 94, 136, 
208, 308, 409, 456, 586, 589, 693, 802, 803, 843, 859, 893, 902, 904, 912, 1209, 
3094, 4093, 9304, 9403, 37, 63, 74, 245, 407, 459, 469, 512, 537, 592, 615, 634, 
674, 704, 742, 753, 754, 794, 915, 932, 942, 953, 954, 42, 84, 204, 206, 207, 306, 
402, 408, 412, 418, 602, 603, 608, 638, 647, 702, 712, 804, 806, 814, 834, 836, 
483, 406, 546, 604, 326, 486, 492, 632, 648, 297, 253, 196, 198, 49, 495, 159, 
396, 23, 165, 367, 108, 927}

print(sorted(test))"""