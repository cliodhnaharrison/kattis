s = input().strip()
while s != "end":
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    line6 = ""
    line7 = ""
    i = 0
    for char in s:
        if char == "0":
            line1 += ("+---+")
            line2 += ("|   |")
            line3 += ("|   |")
            line4 += ("+   +")
            line5 += ("|   |")
            line6 += ("|   |")
            line7 += ("+---+")
        elif char == "1":
            line1 += ("    +")
            line2 += ("    |")
            line3 += ("    |")
            line4 += ("    +")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("    +")
        elif char == "2":
            line1 += ("+---+")
            line2 += ("    |")
            line3 += ("    |")
            line4 += ("+---+")
            line5 += ("|    ")
            line6 += ("|    ")
            line7 += ("+---+")
        elif char == "3":
            line1 += ("+---+")
            line2 += ("    |")
            line3 += ("    |")
            line4 += ("+---+")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("+---+")
        elif char == "4":
            line1 += ("+   +")
            line2 += ("|   |")
            line3 += ("|   |")
            line4 += ("+---+")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("    +")
        elif char == "5":
            line1 += ("+---+")
            line2 += ("|    ")
            line3 += ("|    ")
            line4 += ("+---+")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("+---+")
        elif char == "6":
            line1 += ("+---+")
            line2 += ("|    ")
            line3 += ("|    ")
            line4 += ("+---+")
            line5 += ("|   |")
            line6 += ("|   |")
            line7 += ("+---+")
        elif char == "7":
            line1 += ("+---+")
            line2 += ("    |")
            line3 += ("    |")
            line4 += ("    +")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("    +")
        elif char == "8":
            line1 += ("+---+")
            line2 += ("|   |")
            line3 += ("|   |")
            line4 += ("+---+")
            line5 += ("|   |")
            line6 += ("|   |")
            line7 += ("+---+")
        elif char == "9":
            line1 += ("+---+")
            line2 += ("|   |")
            line3 += ("|   |")
            line4 += ("+---+")
            line5 += ("    |")
            line6 += ("    |")
            line7 += ("+---+")
        elif char == ":":
            line1 += (" ")
            line2 += (" ")
            line3 += ("o")
            line4 += (" ")
            line5 += ("o")
            line6 += (" ")
            line7 += (" ")
        i += 1
        if i != 5:
            line1 += ("  ")
            line2 += ("  ")
            line3 += ("  ")
            line4 += ("  ")
            line5 += ("  ")
            line6 += ("  ")
            line7 += ("  ")

    print (line1)
    print (line2)
    print (line3)
    print (line4)
    print (line5)
    print (line6)
    print (line7)
    print ()
    print ()
    s = input().strip()

print ("end")
