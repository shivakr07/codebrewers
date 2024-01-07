s = str(input())
count = len(set(list(s)))
if count % 2 == 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")