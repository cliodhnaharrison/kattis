import sys

line = sys.stdin.read().strip("\n")


alpha_low = 0
alpha_up = 0
whitespace = 0
symbols = 0

for char in line:
    if char.isalpha() == True and char.islower() == False:
        alpha_up += 1
    elif char.isalpha() == True:
        alpha_low += 1
    elif char == "_":
        whitespace += 1
    else:
        symbols += 1

print ("%0.16f" %(whitespace / len(line)))
print ("%0.16f" %(alpha_low / len(line)))
print ("%0.16f" %(alpha_up / len(line)))
print ("%0.16f" %(symbols / len(line)))
