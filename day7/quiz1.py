# 1. 입력받은 데이터를 이용하여 모든 열의 값 중에서 7 이상의 값을 하나라도 가지고 있는 열을 모두 출력하라
# 요구사항1. 데이터를 리스트로 로딩 후 이 데이터를 매개변수로 하여 ndarry 함수로 변환하고 3*5형태로 변환하여 리턴하는 함수(adata_reshape)를 구성한다
# 요구사항2: 배열 함수의 데이터 행은 정수형으로 바꿔서 사용한다
# 요구사항3: 행의 값 중에서 7 이상의 값을 하나라도 가지고 있는 열 값을 리턴하는 함수(get_data)를 구성한다.

import numpy as np

def get_list_data(infile):
    return [data.strip().split(',') for data in infile]

def adata_reshape(ldata):
    arr = np.array(ldata, dtype=np.int32)
    return arr.reshape(3,5)

def get_data(adata):
    cadata = adata >= 7 # adata의 모든 요소가 7 이상인지 검사하여 True/False로 이루어진 불리언 배열을 생성합니다.
    return adata[:, cadata.any(axis=0)]

data = open('n_quiz1_data.txt', 'r')
input_data = get_list_data(data)
print(input_data, end='\n\n')
data.close()

adata = adata_reshape(input_data)
print(adata, end='\n\n')
adata = get_data(adata)

print(adata)