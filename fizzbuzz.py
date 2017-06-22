import sys

inputstd = sys.stdin.read()

line = inputstd.strip("\n")
values = line.split(" ")

x = int(values[0])
y = int(values[1])
n = int(values[2])

for num in range(1,n+1):
	if num % x == 0:
		if num % y == 0:
			print ("FizzBuzz")
		else:
			print ("Fizz")
	elif num % y == 0:
		print ("Buzz")
	else:
		print (num)
