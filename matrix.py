a=[[1,2,3],[4,5,6],[7,8,9]]
a=[1,2,4,5,6,7,8,9]
print(a)
if any([i <-3 for i in a]) :
    print('true')
else:
    print('false')

if  50 in a :
    print('true')
else:
    print('false')
print(' ' + 'b' + 'c')
xxx=[0,1,2]
yyy=[5,5,5]
print(xxx[0:5])
print(xxx[:1])
print("xxx:{}".format(xxx[:]))
print(xxx)
print("xxx+xxx:{}".format(xxx+xxx))
xxx=["a","b","c"]
zzz=xxx.append(["d"])
print("xxx.append(xxx):{}".format(zzz))
zzz=xxx.append("d")
print("xxx.append(xxx):{}".format(xxx))
xxx.extend('v')
print("xxx.append(xxx):{}".format(xxx))

print(xxx.pop(2))
dict1 = {1:"book", 2:"apple", 3:"eleki"}
print(dict1.keys())
print(dict1.values())
pairs =[[k,v] for k,v in dict1.items()]
print(pairs)
dict1.pop(2)
del dict1[1]
print(dict1.values())