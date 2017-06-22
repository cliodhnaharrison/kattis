import sys

inputstd = sys.stdin.read()

line = inputstd.strip("\n")

binary = format(int(line), 'b')

revbinary = str(binary)[::-1]

rev = int(revbinary, 2)

print (rev)