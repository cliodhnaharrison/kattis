n = int(input())

l = [int(x) for x in input().split()]
alice = 0
bob = 0

while l:
    alice += max(l)
    l.remove(max(l))
    if l:
        bob += max(l)
        l.remove(max(l))

print (alice, bob)
