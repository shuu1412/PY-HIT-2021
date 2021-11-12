s=str(input())
s1=""
cnt=1
s2=""
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        s1=s1+str(cnt)+s[i]
        cnt=1
    else: cnt+=1
s1=s1+str(cnt)+s[len(s)-1]
cnt=1
for i in range(len(s1)-1):
    if s1[i]!=s1[i+1]:
        s2=s2+str(cnt)+s1[i]
        cnt=1
    else: cnt+=1
s2=s2+str(cnt)+s1[len(s1)-1]
print(s1)
print(s2)