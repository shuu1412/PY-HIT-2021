input()
arr = list(map(int, input().split()))
arr2=[]
arr3=[]
arr.sort()
i =0
while (i<len(arr)):
    k=1        
    while (i+1<len(arr) and arr[i]==arr[i+1]):
        i+=1
        k+=1
    arr2.append(arr[i])
    arr3.append(k)
    i+=1
for i in range(len(arr2)):
        print(arr2[i],':',arr3[i])