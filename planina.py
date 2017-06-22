num_iter = int(input())
renum = 2

for _ in range(num_iter):
	renum = (renum + renum - 1)
print (renum * renum)