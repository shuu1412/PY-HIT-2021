def xd10(s: str) ->bool:
    '''
    :params:
    input:
        số cần kiểm tra
    output:
        nếu có '0' or '1' trả về TRUE
        nếu không trả về FALSE
    '''
    if '1' in s or '0' in s:
        return True
    else:
        return False

def ss10(a: str, b: str) ->bool:
    '''
    :params:
    input:
        hai số cần so sánh
    output:
        trả về True nếu 2 số có vị trí của 1 và 0 tương tự nhau
        Nếu không trả về False
    '''
    x = set()
    y = set()
    for i in range(len(a)):
        if a[i]=='1' or a[i]=='0':
            x.add(i)
    for i in range(len(b)):
        if b[i]=='1' or b[i]=='0':
            y.add(i)
    if x==y:
        return True
    else:
        return False
s = list(map(str, input().split()))
ans = []
cnt = 0
for i in range(len(s)):
    if xd10(s[i]):
            ans.append(s[i])

for i in range(len(s)-1):
    for j in range(i+1, len(s)):
        if ss10(ans[i] , ans[j]):
            cnt+=1
print(len(ans)-cnt) 