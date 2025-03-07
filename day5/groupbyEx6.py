import numpy as np
import pandas as pd

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
print(tips.pivot_table(['tip_pct', 'size'],
                       index=['sex', 'smoker'],
                       aggfunc='mean'))
print()
print(tips.pivot_table(['tip_pct', 'size'],
                       index=['sex', 'smoker'],
                       aggfunc=['mean','std']))
print()
print(tips.pivot_table(['tip_pct', 'size'],
                       columns=['sex'], # sex가 열(Column)의 기준이 됨
                       index='day', # day가 행(Row)의 기준이 됨
                       aggfunc='mean'))