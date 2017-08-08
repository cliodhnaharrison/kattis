import sys

input = sys.stdin.read()
line = input.strip("\n")
numbers = line.split()

new_numbers = []
different = False

numbers = sorted([int(x) for x in numbers])
diffs = []

for i in range(len(numbers)):
    if i < len(numbers) - 1:
        diff_new = numbers[i+1] - numbers[i]
        diffs.append(diff_new)

if len(set(diffs)) == 1:
    print numbers[-1] + diffs[0]    
else:
    diff = max(diffs)
    for i in range(len(numbers)):
        if i < len(numbers) - 1:
            diff_new = numbers[i+1] - numbers[i]
            if diff == diff_new:
                print numbers[i] + min(diffs)
