import numpy as np

arr1 = np.arange(0, 10, 1)
print(arr1)
print(type(arr1))

arr2 = np.arange(0,10)
print(arr2)
arr3 = np.arange(10)
print(arr3)

arr4 = np.linspace(-3, 3, 5)
print(arr4)

arr5 = np.ones([3,4]) # 안에 리스트 말고 튜플도 가능
print(arr5)
print()

arr6 = np.zeros((3,4))
print(arr6)
print()

arr7 = np.empty((3,4)) # 초기화해서 안 갖고오고, 같은 크기의 할당한 것이 있다면 그대로 가져다씀(비추~~)
print(arr7)
print()

arr8 = np.full([3,2], 100)
print(arr8)
print()

arr9 = np.ones_like(arr8) # 매개변수의 크기만 참조해서 1로 초기화
print(arr9)
print()

arr9 = np.zeros_like(arr8) # 매개변수의 크기만 참조해서 1로 초기화
print(arr9)
print()

arr9 = np.full_like(arr8, 50) # 매개변수의 크기만 참조해서 1로 초기화
print(arr9)
print()