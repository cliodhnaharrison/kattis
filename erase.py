n = int(input())

before = input()
after = input()

new = ""

for char in before:
    c = char
    for _ in range(n):
        if c == "0":
            c = "1"
        else:
            c = "0"
    new += c

if new == after:
    print ("Deletion succeeded")
else:
    print ("Deletion failed")
