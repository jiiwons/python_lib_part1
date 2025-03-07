# 리스트에 받고
# 더 이상 입력받지 않으면 리스트 다 찍고
# 온디맨드 어레이 찍기

scores = []

while True:
    data = list(map(int,input('국어 영어 수학 점수를 입력하세요:').split(' ')))
    scores.append(data)
    yn = input('입력을 계속 진행하시겠습니까?(y/n)').lower()
    if(yn == 'n'):
        break

print(scores)
print()
import numpy as np

score_arr = np.array(scores)
# print(score_arr)

print('국어 점수: ', score_arr[:, 0])
print('영어 점수: ', score_arr[: , 1])
print('수학 점수: ', score_arr[:, 2])