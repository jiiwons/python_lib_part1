import pandas as pd

frame1 = pd.read_csv('data/ex1.csv') # read_csv는 헤더를 읽어들임

print(frame1)
print(type(frame1))
print()

frame2 = pd.read_csv('data/ex2.csv', header=None)# 헤더가 없다면 컬럼을 자동으로 잡도록 해줌(0,1,2,3,4..)
print(frame2)
print()

frame3 = pd.read_csv('data/ex2.csv', names=['one', 'two', 'three', 'four', 'msg'])
print(frame3)
print()

frame3 = pd.read_csv('data/ex2.csv',
                     names=['one', 'two', 'three', 'four', 'msg'],
                     index_col='msg')
print(frame3)
print()

frame3 = pd.read_csv('data/ex2.csv',
                     names=['one', 'two', 'three', 'four', 'msg'],
                     index_col=0)
print(frame3)
print()

frame4 = pd.read_csv('data/ex4.csv', skiprows=[0,2,3])
print(frame4)
print()

