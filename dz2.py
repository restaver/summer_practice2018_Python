import random
import sys

try:
    n = int(sys.argv[1])
except IndexError:
    print("Error! Enter N")
    n = int(input())
    
sum = 0;
for i in range(n):
    r = random.uniform(-1, 1);
    print ("%.4f"%r);
    sum+=r;
print("average: %.4f"%(sum/n))