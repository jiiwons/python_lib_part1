import pandas as pd
import numpy as np

fec = pd.read_csv('P00000001-ALL.csv')
fec.info()
print()
print(fec.iloc[7])
print()

unique_cands = fec.cand_nm.unique()
print(unique_cands)
print()

# 후보자 이름에 대한 정당을 매치한 딕셔너리
parties = {'Bachmann, Michelle':'Republican',
           'Cain, Herman':'Republican',
           'Gingrich, Newt':'Republican',
           'Huntsman, Jon':'Republican',
           'Johnson, Gary Earl':'Republican',
           'McCotter, Thaddeus G':'Republican',
           'Obama, Barack':'Democrat',
           'Paul, Ron':'Republican',
           'Pawlenty, Timothy':'Republican',
           'Perry, Rick':'Republican',
           "Roemer, Charles E. 'Buddy' III":'Republican',
           'Romney, Mitt':'Republican',
           'Santorum, Rick':'Republican'}

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO',
    'C.E.O.':'CEO'
}

# 정당 칼럼 추가
fec['party'] = fec.cand_nm.map(parties)
print(fec.head())
print()

# 민주당, 공화당에 기부한 사람 수 counting
print(fec['party'].value_counts())

fec = fec[fec.contb_receipt_amt>0]
fec.info()
print()

print(fec.contbr_occupation.value_counts())

cf = lambda x: occ_mapping.get(x, x) # 가져올 x가 없으면 x 그대로
fec.contbr_occupation = fec.contbr_occupation.map(cf)

print(fec.contbr_occupation.value_counts())
print()

# 정당별로 그룹, 왼쪽에느 occup , 기부금액의 합계?
by_occupation = fec.pivot_table('contb_receipt_amt', # 값 → 기부금 액수(contb_receipt_amt)
                                index='contbr_occupation', # 기부자의 직업(contbr_occupation)을 기준으로 그룹화
                                columns='party', # 정당(party)을 기준으로 데이터를 나눔
                                aggfunc = 'sum') # 정당 그룹의 총 기부금 합계 계산
print(by_occupation)
print()
# # 내림차순 정렬
# by_occupation = by_occupation.loc[by_occupation.sum(axis=1).sort_values(ascending=False).index]
# print(by_occupation)


over_2mm = by_occupation[by_occupation.sum(axis=1)>2000000]
print(over_2mm)
print()

# import matplotlib.pyplot as plt
# over_2mm.plot(kind='barh')
# plt.show()

fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
fec_mrbo.info()

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum() # key(여기서는 'contbr_occupation', 즉 직업) 기준으로 contb_receipt_amt(기부금 합계)를 계산
    return totals.sort_values(ascending=False)[:n]

grouped = fec_mrbo.groupby('cand_nm') # cand_nm(후보자 이름)을 기준으로 데이터를 그룹화
print(grouped.apply(get_top_amounts, 'contbr_occupation')) # apply() 함수는 그룹별로 get_top_amounts() 함수를 실행
                                                        # 즉, get_top_amounts(group, 'contbr_occupation')가 오바마 그룹과 롬니 그룹 각각에서 실행됨
print()

bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])
labels=pd.cut(fec_mrbo.contb_receipt_amt,bins)
print(labels)
print()

grouped = fec_mrbo.groupby(['cand_nm', labels]) #  후보자 & 기부금 구간별 그룹화
bucket_sums = grouped.contb_receipt_amt.sum().unstack(level=0) # 각 그룹(후보자별 + 기부금 구간별)에서 총 기부금(contb_receipt_amt)을 합산, level=0 안하고 비교해보기
print(bucket_sums)
print()

# 합산값은 axis=1방향으로, 비율은 개별적으로(각 후보자별로) axis=0
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1), axis=0)
print(normed_sums)