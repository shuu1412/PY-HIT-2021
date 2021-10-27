a= "TRẺTRÂU"
s= input()
j=0
for i in s:
    if j== len(a):
        break
    if i == a[j]:
        j+=1
if j==len(a):
    print("TRẺ TRÂU")
else:
    print("Không TRẺ TRÂU")