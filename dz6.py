import sys , math
 
try:
    infilename = sys.argv [1]
    outfilename = sys.argv [2]
except:
    print "Usage:", sys.argv[0], "infile  outfile"
    sys.exit (1)
 
ifile = open(infilename , 'r')
ofile = open(outfilename , 'w')
  
for line in ifile:
    s = 0; i = 0
    l = line.split ()
    for x in l:
        s+=float(x)
        i+=1
    ofile.write(line +  ' average: %12.6f\n' % (s/i))
ifile.close()
ofile.close()