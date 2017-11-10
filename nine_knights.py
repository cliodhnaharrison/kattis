line1 = input().strip()
line2 = input().strip()
line3 = input().strip()
line4 = input().strip()
line5 = input().strip()

num_knights = line1.count("k") +line2.count("k") + line3.count("k") + line4.count("k") + line5.count("k")
valid = True

board = [list(line1), list(line2), list(line3), list(line4), list(line5)]

if num_knights == 9:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "k":
                if i + 1 in range(0, len(board)-1) and j + 2 in range(0, len(board)-1):
                    if board[i+1][j+2] == "k":
                        valid = False
                if i - 1 in range(0, len(board)-1) and j + 2 in range(0, len(board)-1):
                    if board[i-1][j+2] == "k":
                        valid = False
                if i + 1 in range(0, len(board)-1) and j - 2 in range(0, len(board)-1):
                    if board[i+1][j-2] == "k":
                        valid = False
                if i - 1 in range(0, len(board)-1) and j - 2 in range(0, len(board)-1):
                    if board[i-1][j-2] == "k":
                        valid = False
                if i + 2 in range(0, len(board)-1) and j + 1 in range(0, len(board)-1):
                    if board[i+2][j+1] == "k":
                        valid = False
                if i - 2 in range(0, len(board)-1) and j + 1 in range(0, len(board)-1):
                    if board[i-2][j+1] == "k":
                        valid = False
                if i - 2 in range(0, len(board)-1) and j - 1 in range(0, len(board)-1):
                    if board[i-2][j-1] == "k":
                        valid = False
                if i + 2 in range(0, len(board)-1) and j - 1 in range(0, len(board)-1):
                    if board[i+2][j-1] == "k":
                        valid = False

else:
    valid = False

if valid:
    print ("valid")
else:
    print ("invalid")
