problems = input()

if ";" in problems:
    problems = problems.split(";")
else:
    problems = [problems]

questions = 0

for x in problems:
    if "-" in x:
        x = x.split("-")
        questions+= (int(x[-1]) - int(x[0])) + 1
    else:
        questions += 1

print (questions)
