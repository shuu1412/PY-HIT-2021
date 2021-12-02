import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv("categorical_data.csv")
# print(df)

# Cách 1
imputer = SimpleImputer(missing_values=np.nan , strategy='mean')
df.iloc[:,1:3] = imputer.fit_transform(df.iloc[:,1:3])

"""
SimpleImputer được sử dụng để bổ sung, thay thế dữ liệu bị thiếu

missing_values: giá trị sẽ được thay thế

"""
print("Sử dụng SimpleImputer :\n", df)

# Cách 2

def CalAver(a) :
    sum = 0
    dem = 0
    for i in a :
        if not np.isnan(i) :
            sum=sum+i
            dem=dem+1
    if dem==0 : 
        return None
    return sum/dem

df1 = pd.read_csv('categorical_data.csv')

fill_Age = CalAver(df1.age)
fill_Sal = CalAver(df1.salary)
df1['age'].fillna(value = fill_Age, inplace = True )
df1['salary'].fillna(value=fill_Sal , inplace = True)
'''
Tính các giá trị trung bình cần thay thế

Dùng fillna thay thế NaN thành các giá trị đã tính 
'''
#print(df1)

print("Tính tay :\n " , df1)