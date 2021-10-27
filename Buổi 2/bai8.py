s = input()
x=s.count('1')
if x%2 !=0:
    print("NO")
else:
    x=x/2
    for i in range(len(s)):
        if s[i]=='1':
            x-=1
        if x==0:
            break
    print(s[:i+1],s[i+1:len(s)])
