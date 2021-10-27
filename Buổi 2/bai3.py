#a
s=input('Nhập chuỗi:')
while(len(s)<10):
    s=input('Nhập lại: ')
print(len(s),s[2:7])

#b
s=input('Nhập chuỗi: ')
print(s.upper())
print(s.lower())
print(s.replace('b','g'))

#c
s = "hElLo-mY-NAMe-iS-SuZIe"

print(s.replace('-',' ').title())