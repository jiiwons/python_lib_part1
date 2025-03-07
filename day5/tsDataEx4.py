import pandas as pd
import numpy as np
np.random.seed(12345)

date = pd.date_range('1/1/2020', periods=100, freq='D')
ts = pd.Series(np.random.randn(100), index=date)
print(ts)
print()
rsdata = ts.resample('ME') # 월(Month) 단위로 데이터를 그룹화(리샘플링)
print()

for data in rsdata:
    print(data, end='\n\n')
print()

print(rsdata.mean())
print()

frame = pd.DataFrame(np.random.randn(2,4),
                     index=pd.date_range('1/1/2020', periods=2, freq='W-WED')) # 2020년 1월 1일부터 2주간 매주 수요일(Wednesday) 날짜를 인덱스로 생성
print(frame)
print()
rsdata2 = frame.resample('D') # 일(Daily) 단위로 데이터 리샘플링, 기존에는 매주 수요일 데이터만 존재했으므로, 나머지 요일에는 NaN(결측값) 생성
for data in rsdata2:
    print(data, end='\n\n')

print()
print(frame.resample('D').ffill(limit=2)) # 앞의 값으로 결측값을 채우되, 최대 2개까지만 보간