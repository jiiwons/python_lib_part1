import pandas as pd

frame = pd.DataFrame([(100,90,70),(90,80,60),(70,50,90),(70,100,70)],
                     columns=['kor','eng','math'])
print(frame)

print(frame.corr())
print()
print(frame['kor'].corr(frame['eng']))
print()
print(frame.corrwith(frame['kor']))
print()
print(frame.cov())