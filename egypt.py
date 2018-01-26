while True:
    sides = [int(x) for x in input().split()]

    hypo = max(sides)
    sides.remove(hypo)
    if hypo == 0:
        break
    if hypo**2 == (sides[0]**2 + sides[1]**2):
        print ("right")
    else:
        print ("wrong")
