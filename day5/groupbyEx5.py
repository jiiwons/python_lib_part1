import pandas as pd
import numpy as np

states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
# print(group_key)
data = pd.Series(np.random.randn(8), index=states)
# print(data)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data)
print()

print(data.groupby(group_key).mean()) # East와 West의 평균
# (Ohio + New York + Florida) / 3
# (Oregon + California) / 2
print()

fill_mean = lambda g: g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean))
print()

# 널의 East에는 0.5, West에는 -1
fill_values = {'East':0.5, 'West':-1}
fill_func = lambda g : g.fillna(fill_values[g.name]) # g.name을 이용하여 그룹 이름(East 또는 West)을 가져옴. 해당 그룹의 NaN을 fill_values에서 지정한 값으로 채움.
print(data.groupby(group_key).apply(fill_func))