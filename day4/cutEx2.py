import pandas as pd

scores = pd.Series([70,88,92,54,34,76,59,91,83,78,61,55],
                  index=['홍길동', '이순신', '임꺽정', '정난정', '이이', '이황',
                         '정도전','이성계', '김유신', '김철수', '정약용', '정약전'])
print(scores)

#(8-59:F, 60-69:D, 70-79:C, 80-89:B, 90-100:A)
bins = [8, 60, 70, 80, 90, 100]


rdata = pd.cut(scores, bins, labels=['F', 'D', 'C', 'B', 'A'], right=False)
print(rdata)
print(rdata.value_counts())
print()

print(pd.concat([scores, rdata], axis=1, keys=['점수', '학점']))