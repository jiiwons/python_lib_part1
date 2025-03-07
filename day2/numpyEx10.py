import numpy as np

np.random.seed(12345)
arr = np.random.rand(5, 4)
print(arr)
print()

print(f'평균 : {arr.mean()}') # np.mean(arr)
print(f'합계 : {arr.sum()}') # np.sum(arr)
print(f'표준편차 : {arr.std()}') # np.std(arr)
print(f'분산  : {arr.var()}') # np.var(arr)
print()

print(f'열 평균 : {arr.mean(axis=0)}')
print(f'행 평균 : {arr.mean(axis=1)}')
print()

arr2 = np.array([0,1,2,3,4,5,6,7,8,9])
print(f'누적합: {arr2.cumsum()}')
print()

arr3 = np.array([[0,1,2],
                 [3,4,5],
                 [6,7,8]])
print(f'열 누적곱 : \n{arr3.cumprod(axis=0)}')
print(f'행 누적곱 : \n{arr3.cumprod(axis=1 )}')