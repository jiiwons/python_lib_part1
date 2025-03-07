# 데이터를 입력받은 2차원ndarry로 변환 후 사용한다.
# 변환된 데이터는 각각 열 축으로 누적합한 배열과 행 축으로 누적곱을 한 데이터 두 개를 만든다.
# 이후 누적곱으로 생성된 배열이 누적합으로 생성된 배열보다 각 요소가 더 큰 개수를 출력하라.
#
# 요구사항1: 데이터는 3*3 형태로 재구성한다.
# 요구사항2: 변형된 데이터를 매개변수로 받아 누적합과 누적곱을 리턴하는 함수(get_sum_multi)를 구성한다.
# 요구사항3: 누적합과 누적곱을 이용하여 각 요소를 비교하여 누적곱의 값이 더 큰 요소 개수를 리턴하는 함수(count_func)룰 구성한다.

import pandas as pd
import numpy as np


def get_list_data(infile):
    return [data.strip().split(' ') for data in infile]

def adata_reshape(ldata):
    arr = np.array(ldata, dtype=np.int32)
    return arr.reshape(3,3)

def get_sum_multi(adata):
    arr1 = np.cumsum(adata, axis=0)
    arr2 = np.cumprod(adata, axis=1)
    return arr1, arr2

def count_func(arr1, arr2):
    count = arr2 > arr1
    print(count)
    return count.sum()

infile = open('n_quiz2_data.txt','r')

input_data = get_list_data(infile)
infile.close()

adata = adata_reshape(input_data)
ardata1, ardata2 = get_sum_multi(adata)
output_data = count_func(ardata1, ardata2)

print(output_data)