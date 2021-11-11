s = list(map(int, input().split()))
ans = []
for i in range(len(s)):
    if(s[i]%2==0):
        ans.append(s[i])
    else:
        print(i,end=" ")
print(ans)