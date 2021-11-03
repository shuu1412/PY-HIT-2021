a= set(map(str,input().split()))
b= set(map(str,input().split()))
c=b-a
if len(c):
    print("Không là tập con")
else:
    print("Là tập con")