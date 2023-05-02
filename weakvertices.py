n = int(input())
while n != -1:
  m = []
  for _ in range(n):
    m.append([int(x) for x in input().split()])

  weak = [0] * n
  for i in range(n):
    for j in range(n):
      if m[i][j] and m[j][i] and any([1 if x[i] and x[j] else 0 for x in m]):
        weak[i] = 1

  weak = [str(i) for i in range(n) if not weak[i]]
  print(" ".join(weak))
  n = int(input())
