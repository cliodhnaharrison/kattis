string = input().split()

count = 0.0

for word in string:
    if "ae" in word:
        count += 1.0

if count / float(len(string)) < 0.4:
    print("haer talar vi rikssvenska")
else:
    print("dae ae ju traeligt va")
