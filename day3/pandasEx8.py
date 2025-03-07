import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3,4),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4,5),
                   columns=list('abcde'))
print(df1)
print()
print(df2)
print()

print(df1 + df2)
print()
print(df1.add(df2, fill_value=0))# NaN의 값에 0을 넣어서 더하도록
print()

frame = pd.DataFrame(np.arange(12).reshape(4,3),
                     columns=list('bde'),
                     index=['one', 'two', 'three', 'four'])
print(frame)
print()
sdata = frame.iloc[0]
print(sdata)
print()
print(frame-sdata) # brodcast 연산이 가능