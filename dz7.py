import random

n = 10000
good_resalts = 0
i = 0
while i < n:
    a = random.randrange(1, 7, 1)
    b = random.randrange(1, 7, 1)
    if a == 6 or b == 6:
        good_resalts+=1.0
    i+=1
print (good_resalts/n)