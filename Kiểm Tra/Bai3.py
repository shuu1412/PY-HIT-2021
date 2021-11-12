import math
def check_prime_number(n):
    '''
    :param:
    input:
    1 số nguyên
    output:
    nếu là số nguyên tố trả về 1 còn không thì trả về 0
    '''
    flag = 1;
    if (n <2):
        flag = 0
        return flag 

    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break 
    return flag
n = int(input())
s= list(map(int, input().split()))
cnt = 0
for i in s:
    check = check_prime_number(int(math.sqrt(i)))
    if( check == 1 ) :
        cnt+=1
if cnt == 0:
    print("Không")
else:
    print(cnt)