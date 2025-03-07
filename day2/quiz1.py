names = []
scores = []

while True:
    name = input('이름을 입력하세요:')
    names.append(name)
    data = list(map(int,input('국어 영어 수학 점수를 입력하세요:').split(' ')))
    scores.append(data)
    yn = input('입력을 계속 진행하시겠습니까?(y/n)').lower()
    if(yn == 'n'):
        break

print(scores)
print()
import numpy as np

name_arr = np.array(names)
score_arr = np.array(scores)
# print(name_arr)
print(score_arr)
print()

# print(score_arr.sum(axis=0))
print(f'국어 총점: {score_arr.sum(axis=0)[0]}  영어 총점: {score_arr.sum(axis=0)[1]} 수학 총점: {score_arr.sum(axis=0)[2]} ')

info = input('출력할 학생의 이름을 입력하세요:')
# print(name_arr == info)
print(f'{info} 과목 점수 : {score_arr[name_arr==info][0]}, 평균: {score_arr[name_arr==info].mean():.2f}, 표준 편차: {score_arr[name_arr==info].std():.2f}, 분산: {score_arr[name_arr==info].var():.2f}')