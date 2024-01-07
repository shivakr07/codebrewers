s = str(input())
t = ""
alphabets = ["a","e","i","o","u","y", "A","E","I","O","Y","U"]
for i in s:
    if not(i in alphabets):
        t+=i
t = list(t)
ans = ""
for i in t:
    ans += ("." + i.lower())
print(ans)