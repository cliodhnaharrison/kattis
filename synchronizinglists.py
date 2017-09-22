n = int(input())

while n != 0:
    list1 = []
    list2 = []
    new = [0] * n
    for _ in range(n):
        list1.append(int(input()))
    for _ in range(n):
        list2.append(int(input()))

    order = sorted(list1)
    order2 = sorted(list2)

    for value in list1:
        ord_ind = order.index(value)
        ind = list1.index(value)
        new[ind] = order2[ord_ind]

    for value in new:
        print (value)
    print ()
    n = int(input())
