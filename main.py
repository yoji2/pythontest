import time


try:
    old = time.time()
    print(10)
    for i in range(10000000):
        time_start = time.time()
        if time_start-old >0.1:
            print(i)
            print(time_start-old   )
            old=time_start


except:
    print("errors")
else:
    print("end loop")
finally:
    print(("finished"))
    time.time()
