word = input()
guesses = input()

hang = 0
goal = len(word)

for letter in guesses:
  if hang == 10:
    print("LOSE")
    break
  elif goal == 0:
    print("WIN")
    break

  if letter in word:
    goal -= word.count(letter)
  else:
    hang += 1
