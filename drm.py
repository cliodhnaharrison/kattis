s = input()
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = s[0:int(len(s)/2)]
key = s[int(len(s)/2):]

rotate = sum([alphabet[val] for val in message])

new_message = ""

for val in message:
    start = (alphabet[val] + rotate) % 26
    new_message += a[start]

rotate = sum([alphabet[val] for val in key])

new_key = ""

for val in key:
    start = (alphabet[val] + rotate) % 26
    new_key += a[start]

code = ""

for i in range(len(new_key)):
    pos = (alphabet[new_message[i]] + alphabet[new_key[i]]) % 26
    code += a[pos]

print (code)
