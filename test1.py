a="\x12\x15"
c="aaaa"
print(a)
b=list(a)
print(b)
print(len(a))
print(len(b))
print(len(c))
d=[1,2,3,4,5]
print(d)
e=1
for x  in d:
    if x < 5:
        print("true")
#print(x > 5 in d)
if (e>5):
    print("true")
else:
    print("false")

test = [num for num in range(5)]
print(test)
f=(1,2,3)
print(f)
print(list(f))
#
print('new try')
print( list(range(2,5)))
print(list(range(10,0,-1)))
listx=[]
for i in range(5):
    listx.append(i*0.1)
print(listx)
num = range(1,10)
for x in num:
    listxx=[]
    for y in num:
        listxx.append(y*x)
    print(listxx)

listx = ['apple', 'lemon1', 'suica', 'banana']
listx.sort(key=len)
print(listx)

listx = ['0', '123', '1', '12']
listx.sort(key=int,reverse=True)
print(listx)
listx = ['0', '0123', '01', '012']
listx.sort(key=len)
print(listx)
print("under".upper())
print(sorted(['0', '123', '1', '12']))
f=b'0010'
print(f)
e=8
e=e >>1
e= ~e
print(e)
print(10/4)
print(10 // 4)