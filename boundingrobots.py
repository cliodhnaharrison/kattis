width, length = map(int, input().split())


while length != 0 and width != 0:
    n = int(input())
    robot = [0, 0]
    actual = [0, 0]
    for _ in range(n):
        move, steps = input().split()
        steps = int(steps)
        if move == "u":
            robot[1] += steps
            actual[1] = min(length - 1, max(0, actual[1] + steps))
        elif move == "d":
            robot[1] -= steps
            actual[1] = min(length - 1, max(0, actual[1] - steps))
        elif move == "r":
            robot[0] += steps
            actual[0] = min(width - 1, max(0, actual[0] + steps))
        else:
            robot[0] -= steps
            actual[0] = min(width - 1, max(0, actual[0] - steps))

    print (("Robot thinks {} {}").format(robot[0], robot[1]))
    print (("Actually at {} {}").format(actual[0], actual[1]))
    
    width, length = map(int, input().split())
