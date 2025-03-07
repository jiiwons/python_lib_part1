import pandas as pd
import numpy as np
from pandas import Index

data = pd.DataFrame(np.arange(6).reshape(2,3),
                    index=Index(['ohio', 'colorado'], name='state'),
                    columns = Index(['one', 'two', 'three'], name='number'))
print(data)
result = data.stack() # row로 회전
print()
print(result)
print(type(result)) # 인덱스가 2개인 series
print()

print()
print(result.unstack())
print()
print(result.unstack(level=0))
print()
print(result.unstack('state'))
print()

s1 = pd.Series([0,1,2,3], index=list('abcd'))
s2 = pd.Series([4,5,6], index=list('cde'))
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(data2)
print(data2.unstack())
print(data2.unstack(level=0))