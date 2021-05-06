import pandas as pd

x= pd.read_csv('test.csv')
print(x)
print(x.dtypes)
print(x.columns)
#print(x.loc[0:1,'10'])
x.loc['x'] =[1,2,3]
print(x)
x.to_csv('test.csv')