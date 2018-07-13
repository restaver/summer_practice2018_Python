import random

n = 10000
good_resalts = 0
i = 0
while i < n:
    a = random.randrange(1, 7, 1)
    b = random.randrange(1, 7, 1)
    c = random.randrange(1, 7, 1)
    d = random.randrange(1, 7, 1)
    if (a + b + c + d) < 9:
        good_resalts+=1.0
    i+=1
print 'probability = %f' % (good_resalts/n)
if good_resalts*10 > n:
    print 'agree'
else:
    print 'don\'t agree'