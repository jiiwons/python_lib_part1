import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe'])
print(names)
print(np.unique(names))
print()

values = np.array([6,0, 0, 3, 2, 5, 6])
print(values)
print(np.isin(values, [2,3,6]))
print(np.union1d(values, [2,3,6,8]))
print(np.intersect1d(values, [2,3,4,8]))
print(np.setdiff1d(values, [2,3,6,8]))
print(np.setxor1d(values, [2,3,6,8]))
print()

x = np.array([[1,2,3], [4,5,6]]) # 2 * 3
y = np.array([[6,23],[-1,7],[8,9]]) # 3 * 2
print(x.dot(y))