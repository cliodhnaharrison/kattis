vowels = "aeiou"
s = input()
print (sum([1 for x in s if x in vowels]), sum([1 for x in s if x in vowels or x == "y"]))
