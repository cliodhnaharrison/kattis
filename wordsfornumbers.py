import sys

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[:-1]

units = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
tens = {2 : "twenty", 3 : "thirty", 4 : "forty", 5 : "fifty", 6 : "sixty", 7 : "seventy", 8 : "eighty", 9 : "ninety"}
teens = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen" }

for line in lines:
    line = line.split()
    for i in range(len(line)):
        if line[i].isnumeric() == True:
            num = int(line[i])
            if num // 10 == 0:
                line[i] = units[num]
            else:
                if num // 10 == 1:
                    line[i] = teens[num]
                else:
                    string = ""
                    string += tens[num//10]
                    if num%10 != 0:
                        string += "-" + units[num%10]
                    line[i] = string
    line = " ".join(line)
    first = line[0].upper()
    line = first + line[1:]
    print (line)
