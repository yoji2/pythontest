def func(num):
    
    for i in range(num):
        print("abc")


func(1)

fp = open("test.txt",mode='r')
#line1=fp.read()
#line1 = fp.readline()
line2 = fp.readlines()
print(line2)
#print(line2)
fp.close()

fp = open("test.dat",mode='br')
texts=fp.read()
print(texts)
print(type(texts))
fp.close()

fp = open("writetest.txt","w")
for i in range(10):
    fp.write(str(i)+'\n')

fp.close()