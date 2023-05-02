day, month, year = map(int, input().split("/"))
if day > 12:
  print("EU")
elif month > 12:
  print("US")
else:
  print("either")
