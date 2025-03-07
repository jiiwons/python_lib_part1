import pandas as pd

frame = pd.read_excel('data/monthly_sales.xlsx', header=1, index_col=0)
print(frame)
print()

frame2 = pd.read_excel('data/class_info.xlsx', header=0, sheet_name='2학년')
print(frame2)
print()

frame2 = pd.read_excel('data/class_info.xlsx', header=0, sheet_name=0) # 1학년
print(frame2)
print()

data = pd.read_excel('data/class_info.xlsx', header=0, sheet_name=None) # dict
print(data)
print()

print(data['2학년'])
print()

data = pd.read_excel('data/class_info.xlsx', header=0, sheet_name=['1학년', '2학년'])
print(data)
print()

import numpy as np
frame3 = pd.DataFrame(np.random.randn(100,4) ,
                      columns=['seoul', 'busan', 'incheon', 'suwon'])

frame3.to_csv('sfile.csv')
frame3.to_csv('sfile2.csv', index=False) # 인덱스 제외하고 저장