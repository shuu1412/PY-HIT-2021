a=input()
b=input()
cnt=0
for i in range(len(b)):
    if i+len(a)<=len(b):
        if b.find(a,i,i+len(a))!=-1:
            cnt+=1
print(cnt)