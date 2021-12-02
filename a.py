import numpy as np
import random
# khởi tạo mảng

arr =np.array([(1,2,3,4,5),(6,7,8,9,10)])
print(arr)

a=np.zeros(shape=(3,4),dtype=int) #khoi tao mang voi cac phan tu bang 0
print(a)

b=np.full(shape=(2,3,5),fill_value=2) # khoi tao mang voi gia tri bang 2
print(b)
print(b.shape)
#print(b.ndim)# số chiều ma trận



c=np.random.randint(2,4)
c=random.randint(0,5)
print(c)

load_file = np.loadtxt(fname='Trung.txt')
print(load_file)