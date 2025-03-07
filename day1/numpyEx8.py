import numpy as np

arr = np.arange(8)
print(arr)
print()
arr2 = arr.reshape((4,2))
print(arr2)
print()

ldata = [10,20,30,40,50,60]
arr3 = np.reshape(ldata, (3,2))
print(arr3)
print(type(arr3))
print()

print(arr3.T) # 전치(3,2)을 (2,3)으로 바꿈