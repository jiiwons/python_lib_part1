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
print(name_arr)
print(score_arr)
print()

info = input('출력할 학생의 이름을 입력하세요:')
# print(name_arr == info)
print(score_arr[name_arr==info])