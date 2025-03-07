import pandas as pd

ages = [20,22,25,27,21,23,37,31,61,45,41,70,32]
bins = [18,25,35,60,100]
cdata = pd.cut(ages, bins)
print(cdata)
print(pd.value_counts(cdata))

cdata2 = pd.cut(ages, bins, right=False) # right가 미포함되고, left가 포함됨
print(cdata2)
print(pd.value_counts(cdata2))
print()


rdata = pd.cut(ages, bins, labels=['Youth', 'YoungAdult', 'MiddleAged', 'Senior'])
print(rdata)
print(pd.value_counts(rdata))