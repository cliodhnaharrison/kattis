n = int(input())

for _ in range(n):
    message = input()
    square = int(len(message) ** 0.5)
    box = [message[i:i+square] for i in range(0, len(message), square)]
    original = [""] * len(message)
    for i in range(len(box)):
        start = i
        row = box[i][::-1]
        for char in row:
            original[start] = char
            start += square
    print ("".join(original))
