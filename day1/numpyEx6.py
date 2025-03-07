import numpy as np

np.random.seed(12345)
data = np.random.randn(7, 4)
print(data)

names = np.array(['bob', 'joe','will', 'bob', 'will', 'joe', 'joe'])
print(names)
print()

print(names == 'bob')
print(data[names=='bob'])
print(data[names=='bob',2:])
print(data[names=='bob', 3:])
print()

print(data < 0)
print()
print(data[data<0])
print()

print(names != 'joe')
data[names!='joe'] = 7 #  joe가 아닌 것들은 7, joe는 그대로
print()
print(data) 