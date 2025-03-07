import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(1000,3),
                     columns=['first', 'second', 'third'])

print(frame)
frame.iloc[:4, [1, 2]] = np.nan
print()
print(frame)
print()

print(frame.sum()) # skipna(True) - NaN값이 있으면 스킵해서 계산
print(frame.sum(skipna=False)) # False - NaN값이 있으면 NaN반환
print()
print(frame.std())
print()
print(frame.describe())
print()
frame.info()
print()
print(frame.head(15))
print()
print(frame.tail(15))