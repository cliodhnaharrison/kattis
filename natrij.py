from datetime import datetime
import sys

line = sys.stdin.read()
line = line.split("\n")
line = line[:-1]
a = line[0]
b = line[1]

a = datetime.strptime(a, "%H:%M:%S")
b = datetime.strptime(b, "%H:%M:%S")

if a == b:
    print "24:00:00"
else:
    if (a > b) == True:
        string = str(b - a)
        result = string.split()[-1]
        if len(result) < 8:
            print "0" + result
        else:
            print result
    else:
        result =  str(b - a)
        if len(result) < 8:
            print "0" + result
        else:
            print result
