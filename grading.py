# This solution felt too big/simple for this problem but any shorter/more complex solutions felt like overcomplicating for the sake of it. 
# Looking for a cleaner way of doing this comparison without making it complex for no good reason.

a, b, c, d, e = map(int, input().split())
n = int(input())

if n >= a:
    print("A")
elif n >= b:
    print("B")
elif n >= c:
    print("C")
elif n >= d:
    print("D")
elif n >= e:
    print("E")
else:
    print("F")
