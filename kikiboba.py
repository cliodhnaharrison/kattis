s = input()
b = s.count("b")
k = s.count("k")
if b+k == 0:
    print("none")
elif b == k:
    print("boki")
elif k > b:
    print("kiki") 
elif b > k:
    print("boba")
