#chaching is very  helpful function ,suppose you run a function and it take approx 5 second and if you want to run that
# fuction again it will again take 5 minutes,so to save our time we use this function as second time it will not take time.
#because cahching means it save our function when we call it first now it will not take that much time.
import time
from functools import lru_cache
@lru_cache(maxsize=3) #this is an chache decorator which store the function information now it will not take same time again.
def some_work(n):
    #some task taking n second.
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("now running some work")
    some_work(3)                    #so as we can see it taking same time in 2nd time calling also.now we will use functool.
    print("done...calling again")
    some_work(3)                     # it save max number of function diffirent timesecond means different .
    some_work(4)                     #but the one which got save will not take time later.like in this 3 sec not taken time
    some_work(2)                     # in second print while 4 and 2 sec taken and again at print 3 (3,4,2sec) had not taken time as this three are already save.
    print("called again")
    some_work(3)
    some_work(4)
    some_work(2)
    print("yo")
    some_work(3)
    print("wahh")