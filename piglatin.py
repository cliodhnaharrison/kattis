import sys

input = sys.stdin.read()
lines = input.split("\n")
lines = lines[:-1]

vowels = ["a", "e", "i", "o", "u", "y"]

for phrase in lines:
    new = ""
    for word in phrase.split():
        if word[0] in vowels:
            new += word + "yay" + " "
        else:
            new_word = ""
            cons = ""
            for i in range(len(word)):
                if word[i] not in vowels:
                    cons += word[i]
                else:
                    new_word += word[i:] + cons + "ay"
                    break
            new += new_word + " "
    print new
