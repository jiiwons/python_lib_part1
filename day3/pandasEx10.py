import pandas as pd
import numpy as np

obj1 = pd.Series(np.arange(4), index=list('dabc'))
print(obj1)
print(obj1.sort_index())
print()

frame1 = pd.DataFrame(np.arange(8).reshape(2,4),
                      index=['three', 'one'],
                      columns=list('dabc'))
print(frame1)
print()
print(frame1.sort_index())
print()
print(frame1.sort_index(axis=1))
print()
print(frame1.sort_index(axis=1, ascending=False))
print()

obj2 = pd.Series([4,7,-5,3])
print(obj2)
print()
print(obj2.sort_values())
print()

data = {'second':[4,7,-3,2],'first':[0,1,0,1]}
frame2 = pd.DataFrame(data)
print(frame2)
print()
print(frame2.sort_values(by='second'))
print()
print(frame2.sort_values(by='first'))
print()
print(frame2.sort_values(by=['first', 'second'])) # first로 먼저 sorting을 하고, 만약에 그룹이 생긴다고 하면 second로 정렬해라
print()
print(frame2.sort_values(by=['first', 'second'], ascending=[False, True])) # first는 내림차순, second는 오름차순
