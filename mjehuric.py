s = input().split()

def bubble(l):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]
                print (" ".join(l))

bubble(s)
