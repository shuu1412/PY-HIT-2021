aList = list(map(int , input().split()))
k = int(input())
dem=0
for i in range(len(aList)):
    dem+= aList[i+1:].count(k-aList[i])
print(dem)
