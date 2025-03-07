import pandas as pd
import numpy as np

s1 = pd.Series([0,1], index=list('ab'))
s2 = pd.Series([2,3,4], index=list('cde'))
s3 = pd.Series([5,6], index=list('fg'))
print(s1)
print()
print(s2)
print()
print(s3)
print()

print(pd.concat([s1,s2,s3], axis=0))
print()

print(pd.concat([s1,s2,s3], axis=1)) # concat에서는 붙일 때 조심해서(NaN값 대량 발생)
print()

s4 = pd.concat([s1 * 5, s3])
print(s4)
print()

print(pd.concat([s1, s4], axis=1))
print()
print(pd.concat([s1, s4], axis=1, join='inner')) #inner로 하면 NaN있는 칼럼 삭제

df1 = pd.DataFrame(np.arange(6).reshape(3,2),
                   index=list('abc'),
                   columns=['one', 'two'])
df2 = pd.DataFrame(np.arange(4).reshape(2,2),
                   index=list('ac'),
                   columns=['three', 'four'])
print(df1)
print()
print(df2)
print()
print(pd.concat([df1, df2], axis=1))
print()
print(pd.concat([df1, df2], axis=1, keys=['data1', 'data2'])) # data1 - one, two/ data2 - three, four