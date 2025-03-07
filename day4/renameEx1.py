import pandas as pd
import numpy as np

data =  pd.DataFrame(np.arange(12).reshape(3,4),
                     index=['Ohio', 'Colorado', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
print(data.index.map(str.upper),'\n')
data.index = data.index.map(str.upper)
print(data,'\n')

print(data.rename(index=str.title, columns=str.upper),'\n')
print(data.rename(index={'OHIO':'INDIA'},
                  columns={'three':'peekaboo'}))