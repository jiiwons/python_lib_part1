import numpy as np
import pandas as pd

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']

def g_func(gdata, n=5, column='tip_pct'):
    return gdata.sort_values(by=column, ascending=False)[:n]

# 'smoker' 컬럼을 기준으로 그룹화하고, 각 그룹별 상위 5개 데이터 추출
print(tips.groupby('smoker').apply(g_func))
print()
print(tips.groupby(['smoker', 'day']).apply(g_func, n=3, column='total_bill')) # smoker, day별로 그룹화되어있고, total_bill을 기준으로 정렬되어있으며 각 그룹마다 3개씩 출력