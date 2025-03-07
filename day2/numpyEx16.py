import numpy as np

arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)

print(arr1)
# [[1 2 3]
#  [4 5 6]]
print()
print(arr2)
# [[ 7  8  9]
#  [10 11 12]]
print()

print(np.concatenate([arr1, arr2], axis=0)) # 세로 방향으로
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(np.concatenate([arr1, arr2], axis=1)) # 가로 방향으로
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
print()

print(np.vstack([arr1, arr2]))
print()
print(np.hstack([arr1, arr2]))
print()

arr3 = np.arange(6)
# [0 1 2 3 4 5]
arr4 = np.arange(6).reshape(3,2)
# [[0 1]
#  [2 3]
#  [4 5]]
arr5 = np.random.randn(3,2)
# [[-0.12925738  0.08764092]
#  [ 0.8704605  -0.03886188]
#  [-0.28171853 -0.22279353]]
print(arr3)
print()
print(arr4)
print()
print(arr5)
print()
print(np.r_[arr4,arr5]) # 행(row) 방향으로 배열을 연결 (수직 결합), 행 방향(위-아래)
# [[ 0.          1.        ]
#  [ 2.          3.        ]
#  [ 4.          5.        ]
#  [-0.12925738  0.08764092]
#  [ 0.8704605  -0.03886188]
#  [-0.28171853 -0.22279353]]
print()
print(np.c_[arr4, arr5]) # 열(column) 방향으로 배열을 연결 (수평 결합), 열 방향(좌-우)
# [[ 0.          1.         -0.12925738  0.08764092]
#  [ 2.          3.          0.8704605  -0.03886188]
#  [ 4.          5.         -0.28171853 -0.22279353]]
print()
print(np.c_[np.r_[arr4, arr5], arr3])