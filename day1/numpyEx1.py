import numpy as np

ldata1 = [10,20,30,40]
print(ldata1) # [10, 20, 30, 40] 콤마있음 - 객체가 따로따로 분리되어있고, 링크로 연결되어 있음
print(type(ldata1))
print()

arr1 = np.array(ldata1)
print(arr1) # [10 20 30 40] 콤마없음 - 배열이기 때문에 연속된 형태의 데이터 덩어리로 만들어짐
print(type(arr1))
print()

ldata2 = [[1,2,3,4],[5,6,7,8]]
print(ldata2) # 파이썬은 배열 개념이 없고, 다차원이 존재하지 않음 그래서 [[1, 2, 3, 4], [5, 6, 7, 8]] 이건 2 * 4의 배열이 아니라 리스트 2개가 들어간 객체임
arr2 = np.array(ldata2)
print(arr2)
print(arr2.shape) #(2, 4)
print(arr2.dtype) # int64
print()

ldata3 = [10.4, 23, 655.43, 11]
print(ldata3) # [10.4, 23, 655.43, 11]
arr3 = np.array(ldata3)
print(arr3) # [ 10.4   23.   655.43  11.  ] - 정수가 실수형으로 바뀜(같은 타입으로)
print(arr3.dtype) # float64
arr4 = np.array(ldata3, dtype=np.int32)
print(arr4) # [ 10  23 655  11]
print(arr4.dtype) # int32

arr5 = arr4.astype(np.float64)
print(arr5) # [ 10.  23. 655.  11.]

ldata4 = ['1.23', '322.32', 411]
arr6 = np.array(ldata4)
print(arr6) # ['1.23' '322.32' '411'] - 문자열을 바꾸고 싶으면 dtype=np.float64(정수형은 안됨)