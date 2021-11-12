n =int(input())
s = list(map(int, input().split()))
cnt=0
ans=[]
for i in range(n):
    sum=0
    for j in range(1,s[i]):
        if s[i]%j==0:
            sum+=j
    if sum>s[i]:
        cnt+=1
        ans.append(s[i])
print(cnt)
print(ans)