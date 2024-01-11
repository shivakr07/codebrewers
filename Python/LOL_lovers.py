n =  int(input())
t = str(input())
s = list(t)
flag = 0
if s[0] != s[-1]:
    x = s[-1]
    s.pop()
    flag = 0
    for i in s:
        if i == x:
            flag += 1

else:
    x = s[-1]
    s.pop()
    flag = 0
    for i in s:
        if i == x:
            flag += 1


if flag == 1:
    print(-1)
else:
    print(1)
    
    