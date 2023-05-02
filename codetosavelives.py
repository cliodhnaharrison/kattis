n = int(input())

for _ in range(n):
  a = int(input().replace(" ", ""))
  b = int(input().replace(" ", ""))
  print(" ".join(str(a + b)))
