s = input()
count = 1

while s != "END":
    orig = s
    s = s.split("*")
    s_no_space = s[1:-1]
    even = False
    counts = [item.count(".") for item in s_no_space]
    if len(counts) == 0:
        even = True
    elif len(counts) > 1 and max(counts) == min(counts):
        even = True
    elif orig.count("*") == 2:
        even = True
    if even:
        print (count, "EVEN")
    else:
        print (count, "NOT EVEN")
    s = input()
    count += 1
