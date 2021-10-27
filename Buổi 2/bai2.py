aList = list(map(int, input().split()))
result =[aList[0]]
for i in range(1,len(aList)):
    aList[i]+=aList[i-1]
    result.append(aList[i])

print(result)
