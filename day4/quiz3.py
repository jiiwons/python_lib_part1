import pandas as pd

# names = []
# scores = []
#
# while True:
#     name = input('이름을 입력하세요:')
#     names.append(name)
#     data = list(map(int,input('수학 영어 국어 점수를 입력하세요:').split(' ')))
#     scores.append(data)
#     yn = input('입력을 계속 진행하시겠습니까?(y/n)').lower()
#     if(yn == 'n'):
#         break
#
# print(scores)
# print()
#
# df = pd.DataFrame(scores, index=names, columns=['수학', '영어', '국어']).T
# print(df)

## 강사님 코드

oa = False
ddata = dict()

while True:
    name = input('이름을 입력하세요:')
    scores = list(map(int,input('수학 영어 국어 점수를 입력하세요:').split(' ')))
    ddata[name]=scores
    oa =input('입력을 계속 진행하시겠습니까?(y/n)').lower()
    if (oa == 'n'):
        break

frame = pd.DataFrame(ddata, index=['수학', '영어', '국어'])
print(frame)
print()

print(frame.T.stack())

frame['총점'] = frame.sum(axis=1)
frame['평균'] = frame.iloc[:, :3].mean(axis=1).map(lambda x: round(x,2))  # 총점까지 들어가므로 iloc로 범위 제한
print(frame)