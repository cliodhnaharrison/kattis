message = input()
if ":(" in message:
  if ":)" in message:
    print("double agent")
  else:
    print("undead")
elif ":)" in message:
  print("alive")
else:
  print("machine")
