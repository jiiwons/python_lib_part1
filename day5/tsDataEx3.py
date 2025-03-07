import pandas as pd
import numpy as np
np.random.seed(12345)

ts2 = pd.Series(np.random.randn(1000),
                index=pd.date_range('1/1/2020', periods=1000))
print(ts2)
print()
print(ts2['2021'])
print()
print(ts2['2022-05'])
print(ts2['2022-05-01':'2022-05-10']) # 포함
print()

df1 = pd.DataFrame(np.random.randn(100,4),
                   index=pd.date_range('2020/1/1', periods=100, freq='W-WED'), # 각 주 수요일
                   columns=['one', 'two', 'three', 'four'])
print(df1)
print()

print(pd.date_range(start='4/1/2020', end='6/1/2020'))
print(pd.date_range(end='6/1/2020', periods=20))
print(pd.date_range('1/1/2020', '1/3/2020', freq='4h'))
print(pd.date_range('1/1/2000', '2/1/2000', freq='B')) # 평일만(business day)
print(pd.date_range('1/1/2010', '12/3/2010', freq='BME')) # 매월 마지막 평일(Business Month)
