import numpy as np

arr1 = np.array([[1,2,7], [6,7,9]])
print(arr1)
print()
barr1 = np.array([[True, False, True], [False, False, True]])
print(barr1)
print()

print(arr1[barr1]) # [1 7 9] 같은 위치에 있는 값 중에 True에 해당하는 값
print()

barr2 = np.array([False, True])
print(barr2)
print(arr1[barr2]) #  행 선택, arr1의 1번째 행
# [[6 7 9]]
print()

barr3 = np.array([True, False, True])
print(barr3)
print(arr1[:, barr3]) # 열 선택, 0번째 열, 2번째 열 가져옴
# [[1 7]
#  [6 9]]