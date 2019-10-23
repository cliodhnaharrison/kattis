blimps = []

for i in range(5):
    blimp = input()
    if "FBI" in blimp:
        blimps.append(str(i + 1))

if blimps:
    print (" ".join(blimps))
else:
    print ("HE GOT AWAY!")
