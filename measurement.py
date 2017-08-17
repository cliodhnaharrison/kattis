import sys

statement = sys.stdin.read().strip("\n")
statement = statement.split()
num = int(statement[0])
unit = statement[1]
new_unit = statement[-1]

total = int(num)

converts = [1.0, 1000.0, 12.0, 3.0, 22.0, 10.0, 8.0, 3.0]
units = {'thou': 0, 'th': 0, 'inch': 1, 'in': 1, 'foot': 2, 'ft': 2, 'yard': 3, 'yd': 3, 'chain': 4, 'ch': 4, 'furlong': 5, 'fur': 5, 'mile': 6, 'mi': 6, 'league': 7, 'lea': 7}

unit_ind = units[unit]
new_unit_ind = units[new_unit]

if unit_ind == new_unit_ind:
    print num
elif unit_ind < new_unit_ind:
    num = 1
    while unit_ind != new_unit_ind:
        unit_ind += 1
        num = num / converts[unit_ind]
    print total*num
else:
    num = 1
    while unit_ind != new_unit_ind:
        num = num * converts[unit_ind]
        unit_ind -= 1
    print total*num
