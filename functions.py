import math

x: int = 1000000

i: int = 1

a: int = 1

while x > a:
    if (x/i) > a:
        x /= i
        i += 1
    else:
        x = 0
        i -= 1

#print(i)

y: int = 1000000

a: int = 1

j: int = 2

while y > a:
    if (y / (j * math.log2(j))) < a:
        y = 0
        j -= 1
        print("solution: " + str(j))
    else:
        j +=1
    

print(j)

