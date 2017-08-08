import sys

input = sys.stdin.read()
line = input.split("\n")
line = line[:-1]

sharps = ["A# minor", "A# major", "C# minor", "C# major", "D# minor", "D# major", "F# minor", "F# major", "G# minor", "G# major"]

flats = ["Bb minor", "Bb major", "Db minor", "Db major", "Eb minor", "Eb major", "Gb minor", "Gb major", "Ab minor", "Ab major"]

count = 1

for key in line:
    if key in sharps:
        ind = sharps.index(key)
        print "Case " + str(count) + ": " + str(flats[ind])
    elif key in flats:
        ind = flats.index(key)
        print "Case " + str(count) + ": " + str(sharps[ind])
    else:
        print "Case " + str(count) + ": " + "UNIQUE"
    count += 1
