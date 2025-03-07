import pandas as pd
import numpy as np

data = pd.Series([1, -999, 2, -999, -1000, 3])
print(data)
print()
# print(data.replace([-999,-1000], np.nan))
print(data.replace({-999:np.nan, -1000:0}))

np.random.seed(12345)
data = pd.DataFrame(np.random.randn(1000,4))
print(data.head(10))
print()
print(data.describe())

## 첫번째 방법
data[data>3]=3
data[data<-3]=-3
print()
print(data.describe())

## 두번째 방법
# data2 = np.array([-3,5,7,0,-7,-1,2,-3])
# print(data2)
# print(np.sign(data2)) # 양수에 대해서는 1, 음수에 대해서는 -1, 0에 대해서는 0을 리턴
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())