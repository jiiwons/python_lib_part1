import numpy as np
import pandas as pd

tips = pd.read_csv('tips.csv')
print(tips.head(10))
tips.info()
print()

tips['tip_pct'] = tips['tip']/tips['total_bill']
print(tips.head())
print()

# 성별과 흡연 여부에 따른 그룹핑을 하고, 팁 퍼센트를 가져와서 평균값 출력
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print(grouped_pct.mean())
print()
print(grouped_pct.agg('mean')) # agg이용하면 여러 통계 값을 낼 수 있음
print()
print(grouped_pct.agg(['mean', 'std']))
print()
print(grouped_pct.agg([('gmean', 'mean'), 'std'])) # 이름을 변경해서 사용할 수도 있음
print()

print(grouped.agg({'tip':'max', 'size':'sum'})) #tip에는 max를 적용시키고, size에는 sum을 적용시킴
print()

print(grouped.agg({'tip_pct':['min', 'max'],
                   'size':['sum', 'mean', 'min']}))
print()

print(grouped.agg({'tip_pct':['min', 'max'],
                   'size':['sum', 'mean', 'std']}))