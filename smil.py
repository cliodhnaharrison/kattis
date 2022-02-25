# Pattern matching might be most effective for this, will try later

s = input()

for i in range(len(s)):
    if (s[i] == ":" or s[i] == ";") and i+1 <= len(s) - 1:
        if s[i+1] == ")":
            print(i)
        elif s[i+1] == "-" and i+2 <= len(s) - 1:
            if s[i+2] == ")":
                print(i)
