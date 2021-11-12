s=str(input())
n=int(input())
cnt=1
while(n>0):
    s1=""
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            s1=s1+str(cnt)+s[i]
            cnt=1
        else: cnt+=1
    s1=s1+str(cnt)+s[len(s)-1]
    cnt=1
    print(s1)
    s=s1
    n-=1