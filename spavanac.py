import sys

inputstd = sys.stdin.read()

line = inputstd.rstrip()
n = line.split(" ")

if int(n[1]) > 45:
	print (str(n[0]) + " " + str(int(n[1]) - 45))
else: 
	if int(n[0]) != 0:
		print (str(int(n[0]) - 1) +  " " + str((int(n[1]) + 60) - 45))
	else:
		print ("23" +  " " + str((int(n[1]) + 60) - 45))