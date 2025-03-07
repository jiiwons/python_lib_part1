import pandas as pd
import numpy as np

sd1 = pd.Series(np.arange(5), index=list('abcde'))
print(sd1)
print()

print(sd1.drop(['c', 'e']))
print(sd1) # 원본 변하지 않음
print()

sd1.drop(['c', 'e'], inplace=True)
print(sd1) # 원본 변함
print()

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index=list('abcd'),
                     columns = ['one', 'two', 'three', 'four'])
print(frame)
print()
print(frame.drop('a'))
print()
# print(frame.drop('one', axis=1))
print(frame.drop('one', axis='columns')) # 위에 거랑 같은 결과
print()
print(frame.drop(index='a', columns='one'))
