import numpy as np

np.random.seed(12345)

arr = np.random.randn(100)
print((arr>0).sum())

bools = np.array([[False, False, True, False],
                  [False, False, True, True]])
print(bools.sum())
print()
print(bools.any()) # True
print(bools.any(axis=1)) # [ True  True]
print(bools.any(axis=0)) # [False False  True  True]
print()

print(bools.all(axis=0)) # [False False  True False]
print()

data = np.random.randn(10, 4) * 4
print(data)
print()
# 3보다 큰 값이 하나라도 있으면 그 행 모조리 가져오기
print(data[(data>3).any(axis=1)]) # axis=1은 행을 따라 연산을 수행. 다시 말해, 각 행(row)에서 검사한 결과를 반환