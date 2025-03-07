ldata1 = [10,20,30,40]
ldata2 = [100,200,300,400]
ldata3 = ldata1 + ldata2
print(ldata3) # [10, 20, 30, 40, 100, 200, 300, 400] 링크가 붙어져 있는 형태로 출력
print()

import numpy as np
arr1 = np.array(ldata1)
arr2 = np.array(ldata2)
arr3 = arr1 + arr2
print(arr3) # [110 220 330 440]
print()

arr4 = np.array([[10,20,30],
                [40,50,60]])
arr5 = np.array([[1,2,3],
                [4,5,6]])
print(arr4 + arr5) # 같은 위치에 있는 값들끼리 연산됨
print()
print(arr4-arr5)
print()

print(arr4 * 10)
print()

print(1/arr4)
print()

arr5 = np.array([100,200,300])
print(arr4 + arr5) # 10,20,30에 100,200,300을 더하고
                   # 40,50,60에 100,200,300을 더하는 형태
                   # 행의 크기가 같아야 함
print()

arr6 = np.array([[3,2,8],
                [0,3,7]])
arr7 = np.array([[9,1,7],
                [2,2,8]])
print(arr6)
print()
print(arr7)
print()
print(arr6 > arr7)
print(arr7 > 5)