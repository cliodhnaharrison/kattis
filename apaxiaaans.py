name = input()

new_name = name[0]
last_letter = name[0]

for letter in name[1:]:
	if letter == last_letter:
		continue
	new_name += letter
	last_letter = letter
	
print (new_name)