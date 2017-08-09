import sys

input = sys.stdin.read()
line = input.split("\n")

line = line[1:-1]

count = 1
d = {"a": "2", "b":"22", "c": "222", "d": "3", "e": "33", "f": "333", "g": "4", "h": "44", "i": "444", "j": "5", "k": "55", "l": "555", "m": "6", "n": "66", "o": "666", "p": "7", "q": "77", "r": "777", "s": "7777", "t": "8", "u": "88", "v": "888", "w": "9", "x": "99", "y": "999", "z": "9999", " ": "0"}

for item in line:
    new_str = ""
    for char in item:
        if len(new_str) > 0:
            if new_str[-1] == d[char][0]:
                new_str += " "
                new_str += d[char]
            else:
                new_str += d[char]
        else:
            new_str += d[char]
    print "Case #" + str(count) + ": " + new_str
    count += 1
