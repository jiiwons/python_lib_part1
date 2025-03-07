import pandas as pd
import numpy as np

# sdata1 = pd.Series(['a','b','a','c','d','a','c'])
# print(sdata1)
# print()
# print(sdata1.value_counts())

chunker = pd.read_csv('data/ex6.csv', chunksize=1000)
print(chunker)
print()

# for piece in chunker:
#     print(piece, end='\n\n')
# print(next(chunker)) # 위에 코드랑 똑같음

tot = pd.Series([], dtype=np.float64)
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])




