import numpy as np

x=[1, 2,3,4,5,6,7,8,9]
print(x)
print(type(x))
y=np.array(x)
print(y)
print(type(y))
print(np.shape(y))
a=[[1,2,3],[4,5,6]]
b=np.array(a)
print(np.shape(b))
c=np.arange(0,10).reshape(2,5)
print(np.shape(c))
print(c)
print(np.transpose(c))
print(np.concatenate([c,c],axis=0))
print(np.delete(c,0,axis=1))