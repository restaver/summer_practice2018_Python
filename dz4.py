import sys, math

def argv_ln(arg):
    x = float(arg)
    if arg <= 0:
        print("%g is illegal"%arg)
    else:
        print("ln(%g) = %f"%(arg,math.log(arg)))
    return

argv_ln(12.01)
