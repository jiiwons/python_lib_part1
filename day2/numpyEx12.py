import numpy as np

np.random.seed(12345)

arr = np.random.randn(5,3)
print(arr)
print()
arr.sort(axis=1) # 가로 방향으로 정렬
print(arr)
arr.sort(axis=0) # 세로 방향으로 정렬
print(arr)
print(arr[::-1]) # 배열 거꾸로 출력