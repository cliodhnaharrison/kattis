def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

rings = [int(x) for x in input().split()]
first = rings[0]
rings = rings[1:]

for val in rings:
    ans = str(first // gcd(val, first)) + "/" + str(val // gcd(val, first))
    print (ans)
