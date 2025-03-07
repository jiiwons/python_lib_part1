# 입력 데이터는 지역별 연도별 인구수다. 데이터프레임으록 구성한 후 아래와 조건에 맞게 출력하라.
# 요구사항1: 데이터프레임 구성시 columns은 'Ohio', 'Utah', 'Oregon', 'Texas'로 구성하고 index는 2010-2012(2015)으로 구성한다.
# 요구사항2: 위의 데이터프레임을 전달받아 도시의 인구 최댓값과 평균값으로 구성된 데이터프레임을 리턴하는 함수를 구성한다.
# 이때 이 함수는 apply함수를 이용하여 구성한다.
# 요구사항3: 출력되는 데이터프레임은 소수점 2자리까지 표현한다.
import numpy as np
import pandas as pd

# def get_list_data(infile):
#     return [data.strip().split(',') for data in infile]
#
# def make_array(ldata):
#     arr = np.array(ldata, dtype=np.int32)
#     return arr
#
# def make_dataframe(arr):
#     columns = ['Ohio', 'Utah', 'Oregon', 'Texas']
#     index = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
#     df = pd.DataFrame(arr, columns=columns, index=index)
#     return df
#
# def return_info(df):
#     df['최댓값'] =
#
# infile = open('p_quiz1_data.txt', 'r')
# ldata = get_list_data(infile)
# arr = make_array(ldata)
# df = make_dataframe(arr)
# print(df)

## 강사님 코드
def make_func(x):
    return pd.Series([x.max(), x.mean()], index=['max', 'mean'])

def get_dataframe(path):
    df = pd.read_csv(path, names = ['Ohio', 'Utah', 'Oregon', 'Texas'])
    df = df.rename(index={0:2010, 1:2011, 2:2012, 3:3013, 4:2014, 5:2015, 6:2016})
    print(df, end='\n\n')
    return df

def makeMinMean(df, fvar):
    revalue = df.apply(fvar, axis=0).map(lambda x:'%.2f' % x)
    return revalue

frame = get_dataframe('p_quiz1_data.txt')
outdata = makeMinMean(frame, make_func)
print(str(outdata))