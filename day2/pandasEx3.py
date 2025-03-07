import pandas as pd
import numpy as np

obj1 = pd.Series([4,2,6,9], index=list('abcd')) # 리스트로 문자열을 만들면 ㅔ'a', 'b', 'c', 'd'] 이렇게 변함
print(obj1)
print(obj1['b'])
print(obj1.iloc[1]) # index로 location을 갖고오겠다
print(obj1.iloc[1:3]) # 3번 인덱스 불포함
print(obj1['b':'d']) # d 포함
print()

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=['서울', '부산', '인천', '대구'],
                     columns=['one', 'two', 'three', 'four'])
print(frame)
print(frame.loc['부산']['one'])
print(frame.iloc[1,0])
print(frame.iloc[2:, 2:])
print(frame.loc['인천':'대구', 'three':'four'])
print(frame.loc[['인천','대구'], ['three','four']])
print()

print(frame.loc[:, 'one':'three'])
print(frame.iloc[:, :3])
print(frame.iloc[:, :3][frame.three>5]) # three값이 5보다 큰 행만
