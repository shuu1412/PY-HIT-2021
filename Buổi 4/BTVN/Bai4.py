s=input()
s=s.lower()
ans = set(i for i in s)
if len(ans)>=26:
    print("YES")
else:
    print("NO")