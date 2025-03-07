import numpy as np
import pandas as pd

np.random.randn(12345)

frame = pd.DataFrame(np.random.randn(5,5),
                     index=['joe', 'steve', 'wes', 'jim', 'travis'],
                     columns=list('abcde'))
print(frame)
print()

mapping = {'a':'red', 'b':'red', 'c':'blue', 'd':'blue', 'e':'red'}
grouped1 = frame.groupby(mapping, axis=1) # 열(a,b,c,d,e)을 기준으로 매핑
print()
print(grouped1.sum())
print()

labeling = ['one', 'one', 'one', 'two', 'two'] #joe, steve, wes, jim, travis에 대해서 one,one,one,two,two 레이블 붙임
grouped2 = frame.groupby(labeling) # frame의 인덱스를 labeling에 따라 그룹화
print(grouped2.mean())
print()

grouped3 = frame.groupby(len) # 문자 개수에 따라 매핑 3(joe, wes, jim), 5(steve), 6(travis)
print(grouped3.sum())
print()

print(frame.groupby(lambda x:x[-1]).mean()) # 마지막 글자에 따라 매핑
print()

print(frame.groupby([len, labeling]).min())
