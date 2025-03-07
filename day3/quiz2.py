import pandas as pd
import numpy as np

data = pd.read_csv('data/quiz_data.csv', index_col='name')
print(data)

def f3(x):
    return pd.Series([x.max(), x.min(), x.sum(), x.mean()],
                     index=['최댓값', '최솟값', '총합', '평균'])

result2 = data.apply(f3, axis=0)
# print(result2.map(lambda x:f'{x:.1f}'))
print(result2.map(lambda x: round(x,1)))