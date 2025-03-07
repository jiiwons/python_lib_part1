import pandas as pd
import numpy as np
np.random.seed(12345)

frame1 = pd.DataFrame([[10,20,30],[50,60,70]])
print(frame1)
print()

frame2 = pd.DataFrame([[10,20,30],[50,60,70]],
                      index=['one', 'two'],
                      columns=['first', 'second', 'third'])
print(frame2)
print()
print(frame2.index)
print(frame2.columns)
print(frame2.values) # 못 가져오는 밸류도 있음 사용을 지양

ldata = [('김가', 180, 80), ('이가', 160, 50), ('최가', 170,65), ('오가', 165, 60)]
frame3 = pd.DataFrame(ldata, columns=['이름', '키', '몸무게'],
                      index=[11, 12, 21, 22])
print(frame3)
print()

ddata = {'state':['ohio', 'ohio', 'nevada','nevada'], # 하나의 시리즈
         'year':[2020,2021,2020,2021], # 하나의 시리즈
         'pop':[1.5, 1.7, 3.6, 2.4]} # 하나의 시리즈

frame4 = pd.DataFrame(ddata)
print(frame4)
print()

frame4 = pd.DataFrame(ddata, columns=['year','pop', 'state'],
                      index=['one', 'two', 'three', 'four'])
print(frame4)
print()

print(frame4['state'])
print(type(frame4['state'])) # series
print()
print(frame4.state)
print()

print(frame4.loc['two']) # object
print()
print(frame4['pop']['two']) # 세로 먼저 접근
print(frame4.loc['two']['pop']) # 가로 먼저 접근
print()
print(frame4.year.two)
print(frame4.loc['two'].year) # 잘 쓰는 구조는 아님
print()
print(frame4)
print()

# frame4['area'] = pd.Series([32.323, 32.323, 362.43, 542.43],
#                            index=['one', 'two', 'three', 'four'])
# print(frame4)
frame4['area'] = pd.Series([32.323, 562.43],
                            index=['one', 'three'])
print(frame4)
print()

frame4.loc['five'] = pd.Series([2020,3.3, 'utah', '656.91'],
                               index=frame4.columns)
print(frame4)
print()

frame4.index.name = 'id'
frame4.columns.name = 'info'
print(frame4)