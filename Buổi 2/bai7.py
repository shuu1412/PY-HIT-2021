n = int(input())
ten=[]
dantoc=[]
for i in range(n):
    x,y = input().split()
    ten.append(x)
    dantoc.append(y)
a=0
b=0
ans=""
for i in range(n):
    if dantoc.count(dantoc[i]) > a:
        a=dantoc.count(dantoc[i])
        b=dantoc[i]
for i in range(n):
    if dantoc[i]==b:
        ans=ans + ten[i] +" "
print(ans)


