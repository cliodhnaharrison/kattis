import sys

inputstd = sys.stdin.read()
line = inputstd.split("\n")

marius = line[0]
doctor = line[1]

if doctor.count("a") > marius.count("a"):
	print ("no")
else:
	print ("go")
