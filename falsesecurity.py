import sys

lines = sys.stdin.read().split("\n")[:-1]

alphamorse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '_': '..--', ',': '.-.-', '.': '---.', '?': '----'}

morsealpha = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '..--': '_', '.-.-': ',', '---.': '.', '----': '?'}

for line in lines:
    length = ""
    new = ""
    for char in line:
        length += str(len(alphamorse[char]))
        new += str(alphamorse[char])
    i = 0
    prev = 0
    word = []
    length = length[::-1]
    for l in length:
        i += int(l)
        new_char = new[prev:i]
        prev += int(l)
        word.append(new_char)
    answer = ""
    for char in word:
        answer += str(morsealpha[char])
    print (answer)
