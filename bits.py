n = int(input())

for _ in range(n):
    binary = input()
    bits = 0
    for i in range(1, len(binary) + 1):
        check = int(binary[:i])
        bits = max(bits, bin(check).count('1'))
    print (bits)
