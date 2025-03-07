import numpy as np
np.random.seed(12345)

values = np.array([5,0,1,3,2])
indexer = values.argsort() # values값에 맞춰 정렬 후, 인덱스를 출력
print(indexer)
print()

arr = np.random.randn(3,5)
arr[0] = values
print(arr)
print(arr[:, arr[0].argsort()]) # 첫 번째 행을 기준으로 열을 정렬
# arr[:, ...]: 전체 행을 유지한 상태에서 열을 특정 순서대로 정렬
# arr[0].argsort()를 이용해 열의 순서를 재배치

data = np.arange(30).reshape(5,6)
np.random.shuffle(data)
print(data)
print()

print(data[data[:,0].argsort()])
print(data[np.argsort(data[:,0])])