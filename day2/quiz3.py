# 필요한 데이터 16개 - 데이터프레임1개
# ㄱ. 1번째 행 데이터를 조회
# ㄴ. 1번째와 3번째 행 데이터를 조회
# ㄷ. '윤봉길'행만 조회
# ㄹ. '이봉창'과 '윤봉길'행을 조회
# ㅁ. '윤봉길' 행의 '은평구'데이터만 조회
# ㅂ.'김구'와 '이봉창'의 '용산구'와 '은평구'데이터 조회
# ㅅ.'은평구'의 값이 100 이하인 행들을 조회
# ㅇ.'은평구'의 값이 100인 행들을 조회
# ㅈ.'김구'부터 '안중근'까지 '용산구' 데이터를 80으로 변경

import pandas as pd
import numpy as np

myindex = ['김구', '이봉창', '안중근', '윤봉길']
mycolumns = ['강남구', '은평구', '마포구', '용산구']
mylist = list(10 * onedata for onedata in range(1,17))

array_2d = np.array(mylist).reshape(4, 4)

df = pd.DataFrame(array_2d, index=myindex, columns=mycolumns)
# 위 두 줄을 통째로 아래처럼 쓸 수 있음
#df = pd.DataFrame(np.reshape(mylist, (4,4)), index=myindex, columns=mycolumns)

print(df)
print()
# ㄱ. 1번째 행 데이터를 조회
print('ㄱ. 1번째 행 데이터를 조회')
print(df.iloc[1])
print()

# ㄴ. 1번째와 3번째 행 데이터를 조회
print('# ㄴ. 1번째와 3번째 행 데이터를 조회')
print(df.iloc[[1,3]])
print()

# ㄷ. '윤봉길'행만 조회
print("ㄷ. '윤봉길'행만 조회")
# print(df.loc['윤봉길']) # 아래랑 비교해보기([], [[]]의 차이)
print(df.loc[['윤봉길']])
print()

# ㄹ. '이봉창'과 '윤봉길'행을 조회
print("ㄹ. '이봉창'과 '윤봉길'행을 조회")
print(df.loc[['이봉창', '윤봉길']])
print()

# ㅁ. '윤봉길' 행의 '은평구'데이터만 조회
print("ㅁ. '윤봉길' 행의 '은평구'데이터만 조회")
# print(df.loc['윤봉길']['은평구']) # 데이터만
print(df.loc[['윤봉길'],['은평구']]) # 데이터프레임 형태로
print()

# ㅂ.'김구'와 '이봉창'의 '용산구'와 '은평구'데이터 조회
print("ㅂ.'김구'와 '이봉창'의 '용산구'와 '은평구'데이터 조회")
print(df.loc[['김구', '이봉창'],['용산구', '은평구']])
print()

# ㅅ.'은평구'의 값이 100 이하인 행들을 조회
print("ㅅ.'은평구'의 값이 100 이하인 행들을 조회")
# print(df.loc[df.은평구<=100])
print(df.loc[df['은평구']<=100])
print()

# ㅇ.'은평구'의 값이 100인 행들을 조회
print("ㅇ.'은평구'의 값이 100인 행들을 조회")
# print(df.loc[df.은평구==100])
print(df.loc[df['은평구']==100])
print()

# ㅈ.'김구'부터 '안중근'까지 '용산구' 데이터를 80으로 변경
print("ㅈ.'김구'부터 '안중근'까지 '용산구' 데이터를 80으로 변경")
df.loc['김구':'안중근','용산구'] = 80 # '김구'부터 '안중근'까지의 '용산구' 열을 80으로 변경 (Series 형태로 변경됨)
df.loc['김구':'안중근', ['용산구']] = 80 # '김구'부터 '안중근'까지의 '용산구' 열을 80으로 변경 (DataFrame 형태 유지), 연산 후 데이터 구조를 유지하려면 리스트로 감싸는 것이 좋음
print(df)