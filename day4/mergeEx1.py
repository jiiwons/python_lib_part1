import pandas as pd

frame1 = pd.DataFrame({"kdata":["b","b","a","c","a","a","b"],
                       "data":range(7)})
frame2 = pd.DataFrame({"kdata":["a","b","d"],
                       "data2":range(3)})
print(frame1)
print()
print(frame2)
print()

print(pd.merge(frame1, frame2, on="kdata")) # inner join방식(default, how), on: 키를 지정
print()

print(pd.merge(frame1, frame2, on="kdata", how="outer"))
print()

print(pd.merge(frame1, frame2, on="kdata", how="left"))
print()

print(pd.merge(frame1, frame2, on="kdata", how="right"))
print()

frame3 = pd.DataFrame({"lkdata":["b","b","a","c","a","a","b"],
                       "data":range(7)})
frame4 = pd.DataFrame({"rkdata":["a","b","d"],
                       "data2":range(3)})
print(pd.merge(frame3, frame4, left_on="lkdata", right_on="rkdata").drop('rkdata', axis=1))
