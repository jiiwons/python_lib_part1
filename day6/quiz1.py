# 1. 입력 데이터는 학생의 기말고사 성적이다. 이때 이 데이터의 수, 평균 성적, 평균 성적 이상인 비율을 출력하라
# 요구사항1: 파일 객체로부터 리스트 객체로 데이터를 돌려주는 함수(get_list_data)를 사용한다.
# 요구사항2: 리스트 데이터를 전달받아 값을 조건 값들을 추출하고 출력하는 함수(grade_out_func)를 구성한다.
# 요구사항3: 데이터 수는 정수, 평균 성적을 소수점 1자리까지 표현하는 실수, 평균 성적 이상인 비율은 소수점 2자리까지 표현하는 실수로 출력한다.

data = open('quizdata1.txt', 'r')

def get_list_data(infile):
    data.seek(0)
    ldata = list(map(int, [line.rstrip() for line in infile]))
    return ldata

def grade_out_func(ldata):
    count = len(get_list_data(ldata))
    mean = sum(get_list_data(ldata))/len(get_list_data(ldata))
    great = [x for x in get_list_data(data) if x > mean]
    great_ratio = len(great)/count*100
    return count, round(mean,1), round(great_ratio,2)

print(get_list_data(data))
# print('데이터의 수', len(get_list_data(data)))
# mean = sum(get_list_data(data))/len(get_list_data(data))
# print('평균',mean)
#
# great = [x for x in get_list_data(data) if x > mean]
# print(len(great)/len(get_list_data(data))*100)
# print('평균 성적 이상인 비율',great)

print(f'데이터의 수 : {grade_out_func(data)[0]}, 평균 성적 : {grade_out_func(data)[1]}, 평균 성적 이상인 비율 : {grade_out_func(data)[2]}')


### 강사님 코드 추가하기