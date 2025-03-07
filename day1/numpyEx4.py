import numpy as np

arr1 = np.array([9,5,7,1,2,4,6,8])
print(arr1[0])
print(arr1[-1])
print(arr1[2:5])
print()

arr2 = np.array([[2,3,6,8],
                 [3,5,9,7],
                 [0,10,20,30]])
print(arr2)
print()
print(arr2[1,0]) # 1번 행에 0번 열
print(arr2[1][0]) # 이건 가져올 때 arr[1]을 먼저 가져온 후, 한 행으로 만들어서(1차원) 0번째를 가져오는 것임
print()
print(arr2[1:, 2:])
print(arr2[1:][2:]) # 빈 객체 반환 