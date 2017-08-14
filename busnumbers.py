n = int(input())
buses = sorted(map(int, input().split()))

buses.append(10000000000)

chain = 1
prev = buses[0]

output = []
i = 1
while i < len(buses):
    current = buses[i]
    if current == prev + 1:
        chain += 1
    else:
        if chain >= 3:
            output.append(str(buses[i-chain]) + "-" + str(buses[i-1]))
        elif chain == 2:
            output.append(buses[i-2])
            output.append(buses[i-1])
        else:
            output.append(buses[i-1])
        chain = 1
    prev = current
    i += 1

print(' '.join([str(i) for i in output]))
