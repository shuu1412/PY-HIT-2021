s = input()
ans = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if (s.count(s[i:j])>=2):
            ans=max(ans,j-i+1)
print(ans)