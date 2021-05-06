import pandas as pd

data={
    'name':['A','B','C'],
    'weight':[1,10,100],
    'nick':[10,12,8]
}
df=pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df.columns)
print(df.tail(2))
print(df.head(1))
print(df.sort_values(by='nick'))
print(df.loc[:, 'name'] )
print(df.loc[1:1, :] )
print(df.query('name=="B"'))


#df.loc('name')

#data sort
'''
import numpy as np

df =pd.DataFrame(np.random.rand(5,1))
print(df)
print(df.dtypes)
print(df.columns)
print(df.sort_values(by=0))

print(df)

'''