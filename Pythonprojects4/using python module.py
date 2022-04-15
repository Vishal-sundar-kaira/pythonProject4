#about modules
import random
random_number=random.randint(0,10)
print(random_number)
#random choice
list=("vishal","sahil","bittu","abhishek")
choice=random.choice(list)
print(choice)

#time modules
import time
initial=time.time()
print(initial)               #this will give particular time and after that time will start increasing by 1 seconds
k=0                          # so for time we always need to apply function whose time you need minus(-)initial
while(k<50):
    k+=1
    print("yo kaisan baa")
print("time taken by while loop is",time.time()-initial,"seconds")

for i in range(50):
    print("hello guys its vishal here")
print("time taken by for loop is",time.time()-initial,"seconds")

# localtime=time.asctime()
# print(localtime)
from pygame import mixer
mixer.init()
mixer.music.load("alarm.mp3.wav")
mixer.music.play()
