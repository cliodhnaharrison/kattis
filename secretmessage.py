n = int(input())

for _ in range(n):
    original = input()
    square = int(len(original) ** 0.5)
    while True:
        if square ** 2 >= len(original):
            break
        else:
            square += 1
    if square ** 2 > len(original):
        original += ("*" * int((square ** 2) - len(original)))

    box = [original[i:i+square] for i in range(0, len(original), square)]
    message = [""] * len(original)
    start = 0
    for i in range(len(box)):
        row = box[i][::-1]
        j = 0
        for char in row:
            message[start + j] = char
            j += square
        start += 1
    print ("".join(message[::-1]).replace("*", ""))
