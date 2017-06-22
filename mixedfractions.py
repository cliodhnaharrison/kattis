import sys

inputstd = sys.stdin.read()

line = inputstd.replace("\n", "n")
values = line.split("n")
values = values[:-1]

for item in values:
	if item[0] != "0":
		item = item.split()
		whole_num = str(int(item[0]) // int(item[1]))
		top_num = str(int(item[0]) % int(item[1]))
		fraction = whole_num + " " + top_num + " / " + str(item[1])
		print (fraction)