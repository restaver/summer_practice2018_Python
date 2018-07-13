import sys , math

try:
    filename = sys.argv [1]
except:
    print "Usage:", sys.argv[0], "outfile"
    sys.exit (1)

ofile = open(filename , 'w')

def  myfunc(y):
    if y  >= 0.0:
        return y**5* math.exp(-y)
    else:
        return  0.0

i = 2
while i+1 < len(sys.argv):
    x = float(sys.argv[i])
    y = float(sys.argv[i+1])
    fy = myfunc(y)
    ofile.write('%g %12.5e\n' % (x,fy))
    i+=2

ofile.close()