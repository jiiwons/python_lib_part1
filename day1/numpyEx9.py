import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# True면 x를 가져오고, False이면 y를 가져오도록
# 컴프리헨션 이용
result = [x if c else y for x, y, c in zip(xarr, yarr, cond)]
print(result)

# 위에 걸 좀 더 쉽게 : where
result2 = np.where(cond, xarr, yarr)
print(result2)
print()

np.random.seed(12345)
arr = np.random.randn(4,4)
print(arr)
print()
print(np.where(arr>0, 2, -2))
print()
print(np.where(arr>0, 2, arr))
print()

data = np.array([3,6, 4,5,6,7, 6])
print(np.where(6==data))