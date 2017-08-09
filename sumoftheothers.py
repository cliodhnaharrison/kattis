import sys
import copy

input = sys.stdin.read()
tests = input.split("\n")
tests = tests[:-1]

for case in tests:
    case = [int(x) for x in case.split()]
    sum_total = 0
    for num in case:
        temp_list = copy.deepcopy(case)
        temp_list.remove(num)
        if sum(temp_list) == num:
            sum_total = num
    print sum_total
