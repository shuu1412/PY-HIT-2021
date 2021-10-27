s = input()
while len(s) >1:
    x=0
    for i in s:
        x+=int(i)
    s=str(x)
print(s)