from math import floor
highestPower = 6
palSum = 0
parPower = 0
oddPower = 0

def isBinPal(n):
    binN = bin(n)
    bl = len(binN)
    for i in range(floor(bl/2)-1):
        if not binN[i+2] == binN[bl-i-1]:
            return False
    print(n)
    return True


for power in range(highestPower+1):
    if power % 2 == 0:
        for i in range(max(1,10**(parPower-1)),10**parPower):
            num = str(i)
            pal = int(num + num[::-1])
            if(isBinPal(pal)):
                palSum += pal
        parPower += 1
    else:
        for i in range(10):
            if power == 1:
                pal = i
                if (isBinPal(pal)):
                    palSum += pal
            elif power > 1:
                for k in range(10**(oddPower-1),10**oddPower):
                    num = str(k)
                    pal = int(num + str(i) + num[::-1])
                    if power == 0:
                        pal = k

                    if (isBinPal(pal)):
                        palSum += pal
        oddPower += 1


print (palSum)
