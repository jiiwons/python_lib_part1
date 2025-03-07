# 클래스 만들어서 이름, 점수 입력받아서 객체에 저장

class ExamScore:
    count = 0
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        ExamScore.count+=1 # 객체가 호출될때마다 카운트 증가

    def print_info(self):
        print(f'name:{self.name}')
        print(f'국어:{self.kor}, 영어:{self.eng}, 수학:{self.math}', end='\n\n')


    def total_score(self):
        return self.kor + self.eng + self.math


yn=''
obj_list = []
while True:
    name = input('이름을 입력하세요:')
    scores = list(map(int, input('국어 영어 수학 점수를 입력하세요:').split()))
    obj_list.append(ExamScore(name, scores[0], scores[1], scores[2]))
    yn = input('계속 입력하시겠습니까?(y/n):')
    if yn.lower() == 'n':
        break

for obj in obj_list:
    obj.print_info()

total_score = 0
for obj in obj_list:
    total_score +=obj.total_score()
print(f'전체 총점 : {total_score}, 평균:{total_score/ExamScore.count:.2f}')