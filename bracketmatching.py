n = int(input())
s = input()
opening = "([{"
closing = ")]}"
tmp = []
valid = True

if n % 2 != 0:
  valid = False
else:
  for i in range(n):
    if len(tmp) == 0:
      if s[i] in closing:
        valid = False
        break
      tmp.append(s[i])
    elif s[i] in closing:
      if closing.index(s[i]) == opening.index(tmp[-1]):
        tmp.pop()
      else:
        valid = False
        break
    else:
      tmp.append(s[i])

if valid and len(tmp) == 0:
  print("Valid")
else:
  print("Invalid")
