import sys, math

def argv_ln(arg):
    x = float(arg)
    if x <= 0:
        print("%g is illegal"%x)
    else:
        print("ln(%g) = %f"%(x,math.log(x)))
    return

print("first loop:")
for r in sys.argv[1:]:
    argv_ln(r)

print("\nsecond loop:")
for i in range(1, len(sys.argv)):
    argv_ln(sys.argv[i])

print("\nthird loop:")
i = 1
while i < len(sys.argv):
    argv_ln(sys.argv[i])
    i+=1

print("\nfourth loop:")
i = 1
while 1:
    try:
        argv_ln(sys.argv[i])
    except IndexError:
        break
    i+=1