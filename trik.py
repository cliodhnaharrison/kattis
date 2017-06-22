import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "")

ball = 1

for move in line:
	if move == "A":
		if ball == 1:
			ball = 2
		elif ball == 2:
			ball = 1
		elif ball == 3:
			ball = 3
	elif move == "B":
		if ball == 1:
			ball = 1
		elif ball == 2:
			ball = 3
		elif ball == 3:
			ball = 2
	
	elif move == "C":
		if ball == 1:
			ball = 3
		elif ball == 2:
			ball = 2
		elif ball == 3:
			ball = 1
			
			
print (ball)
