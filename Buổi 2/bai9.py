s= input().split(",")
a=[]
b=[]
for i in s:
    if int(i[1:-1])%2:
        b.append(int(i[1:-1]))
    else:
        a.append(int(i[1:-1]))
print(tuple(a+b))