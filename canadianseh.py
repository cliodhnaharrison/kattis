# https://open.kattis.com/problems/canadianseh

s = input()[-3:]
if s == "eh?":
    print("Canadian!")
else:
    print("Imposter!")
