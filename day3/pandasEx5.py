import pandas as pd
import numpy as np

obj1 = pd.Series([4,7,-5,5], index=list('dabc'))
print(obj1)
print()

obj2 = obj1.reindex(list('abcde'))
print(obj2)
print()

obj3 = pd.Series(['blue', 'purple','yellow'], index=[0,2,4])
print(obj3)
print()

obj4 = obj3.reindex(np.arange(6), method='ffill') # 빈 값을 앞에 있는 값으로 채움(보간메소드)
print(obj4)
print()

frame = pd.DataFrame(np.arange(9).reshape(3,3),
                     index=list('acd'),
                     columns=['ohio', 'texas', 'california'])
print(frame)
print()
print(frame.reindex(list('abcd')))
print()
print(frame.reindex(columns=['texas', 'utah', 'california']))
print()
print(frame.reindex(index=list('abcd'), columns=['texas', 'utah', 'california']))