from datetime import datetime
import pandas as pd
import numpy as np
np.random.seed(12345)

dates = [datetime(2024, 1, 1), datetime(2024, 1, 2), datetime(2024, 1, 3),
         datetime(2024, 1, 4), datetime(2024, 1, 5), datetime(2024, 1, 6),
         datetime(2024, 1, 7), datetime(2024, 1, 8)]

ts = pd.Series(np.random.randn(8), index=dates)
print(ts)
print()

print(ts['2024-01-03'])
print(ts['2024/01/03'])
print(ts['20240103']) # 비추
print(ts['1/03/2024'])
print(ts['01-03-2024'])
