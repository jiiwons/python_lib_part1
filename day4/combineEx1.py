import pandas as pd
import numpy as np

s1 = pd.Series([np.nan, 2.5, np.nan, 4.5, 5.5, np.nan],
               index=list('fedcba'))
s2 = pd.Series(np.arange(len(s1), dtype=np.float32),
               index=list('fedbca'))
print(s1)
print()
print(s2)
print()
print(np.where(pd.isnull(s1), s2, s1)) # s1이 널이면 s2를 넣고, 그렇지 않으면 원래 s1 값을 유지
print()

print(s1.combine_first(s2))
print()

df1 = pd.DataFrame({'d1':[1., np.nan, 5., np.nan],
                    'd2':[np.nan, 2., np.nan, 6.],
                    'd3':range(2,18,4)})
df2 = pd.DataFrame({'d1':[5., 4., np.nan, 3., 7.],
                    'd2':[np.nan,3., 4.,6., 8.]})

print(df1)
print()
print(df2)
print()

print(df1.combine_first(df2))
print()
print(df1.combine_first(df2.iloc[:4])) # 필요한 부분까지만 지정