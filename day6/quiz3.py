# obj_list를 저장할 수 있는 클래스를 만들어서 iterator를 구현하기

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


class ScoreList:
    def __init__(self):
        self.slist = [] # 학생 객체들을 저장할 리스트
        self.index = 0 # 이터레이터 인덱스

    def addObject(self, item):
        self.slist.append(item) # 학생 객체 추가

    def __iter__(self): # 반복 가능한 객체임을 알려주며, 보통 self를 반환.
                        # for 문이 실행될 때 한 번만 호출됨.
        return self # self를 반환하여 이터레이터 역할 수행(자기 자신을 반환 -> 이터레이터로 사용 가능)

    def __next__(self): # for 문이 실행될 때마다 호출되어 다음 데이터를 반환.
        if self.index < len(self.slist): # 리스트 범위 내에 있다면
            revalue = self.slist[self.index] # 현재 인덱스의 객체 반환
            self.index += 1 # 인덱스 증가
            return revalue
        else: # 리스트를 다 순회했다면
            self.index = 0 # 인덱스를 초기화하여 다시 순회 가능하도록 설정
            raise StopIteration # 이터레이션 종료
        
yn=''
sldata = ScoreList()
while True:
    name = input('이름을 입력하세요:')
    scores = list(map(int, input('국어 영어 수학 점수를 입력하세요:').split()))
    sldata.addObject(ExamScore(name, scores[0], scores[1], scores[2]))
    yn = input('계속 입력하시겠습니까?(y/n):')
    if yn.lower() == 'n':
        break

for obj in sldata:
    obj.print_info()

total_score = 0
for obj in sldata:
    total_score +=obj.total_score()
print(f'전체 총점 : {total_score}, 평균:{total_score/ExamScore.count:.2f}')