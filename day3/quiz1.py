import pandas as pd

data = {
    '번호':[1,2,3,4,5,1,2,3,4,5],
    '반':['A','A','A','A','A','B','B','B','B','B'],
    '영어':[100,90,100,80,70,90,100,70,80,90],
    '국어':[90,80,90,70,100,80,90,100,70,80],
    '수학':[80,100,80,90,80,100,70,80,90,100]
}
# df = pd.DataFrame(data)
# print(df)
#
# # 각 학생의 평균
# score = df.drop(columns=['번호', '반'])
# score_sum = round(score.sum(axis=1)/3,2)
# # print(score_sum)
# df['평균'] = score_sum
# print(df)
#
# # 각 과목의 평균
# subject =  df.drop(columns=['번호', '반', '평균'])
# subject_sum = round(subject.sum()/10,2)
# print(subject_sum)

#### 강사님 코드
df_score = pd.DataFrame(data, columns=['반', '번호', '국어', '영어', '수학'])
print(df_score)
print()

df_score.drop(['반', '번호'], axis=1, inplace=True)
print(df_score)
df_score['평균'] = df_score.mean(axis=1)
print(df_score)
print()

df_score.loc['평균'] = df_score.mean(axis=0) # 아래 방향으로 넣어야 하니까 loc사용
print(df_score)