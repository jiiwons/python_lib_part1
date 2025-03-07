# 미국 도시의 대한민국 도시 인구 수 입력 데이터를 이용하여 데이터프레임으로 구성한다. 미국 도시의 인구 평균과 대한민국 도시들의 평균을 아래의 조건에 맞게 출력하라.
# 요구사항1:미국 도시와 대한민국 도시의 인구 평균 구하는 함수(city_group_data)를 구성한다.
# 요구사항2: 평균 값은 데이터프레임의 인덱스 기준으로 한다.
# 요구사항3: 출력값은 소수점 1자리까지 표현한다.
import pandas as pd

def get_dataframe(path):
    df = pd.read_csv(path)
    return df

# 매핑이 포인트였음
def city_group_data(df):
    mapping = {'ohio':'us', 'seoul':'kor', 'daegu':'kor', 'texas':'us'}
    grouped = df.groupby(mapping, axis=1).mean().map(lambda x:round(x,1))
    return grouped

frame = get_dataframe('p_quiz2_data.txt')
print(frame)
outdata = city_group_data(frame)
print(str(outdata))