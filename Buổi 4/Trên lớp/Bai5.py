s = list(map(int,input().split()))
x = int(input())
def Pa():
    if x in s:
        print(s.index(x))
        s.remove(x)
Pa()
def Pb():
    while (x in s):
        s.remove(x)
Pb()
y = int(input())
def Pc():
        s[y]=x
Pc()