import time
from threading import Thread


def myfunc(n):
    print("sleeping 5 sec from thread {i}".format(i=n))
    time.sleep(5)
    print("finished sleeping from thread {i}".format(i=n))


for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
