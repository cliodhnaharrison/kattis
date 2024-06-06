n = input().replace("0", "")
ready = False
answer = 1

if len(n) == 1:
  print(n)
  ready = True

while not ready:
  for x in n:
    answer *= int(x)
  answer = str(answer).replace("0", "")
  if len(answer) < 2:
    print(answer)
    ready = True
  n = answer
  answer = 1
