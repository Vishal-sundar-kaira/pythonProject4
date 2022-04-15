from datetime import datetime
from pygame import mixer
from time import time
def musiconloop():
    mixer.init()
    mixer.music.load("alarm.mp3.wav")
    mixer.music.play()
    while True:
        a = input()
        if a == "done":
            mixer.music.stop()
            break




def log_now(msg):
    with open("healthyprogrammer.txt","a")as f:
        a=f.write(f"{msg}work at{datetime.now()}\n")
        print(a)

if __name__ == '__main__':
    init_water=time()
    init_exercise=time()
    init_eye=time()
    watersec=10*3
    exercisesec=20*3
    eyesec=30*3
    while True:
        if time()-init_water>watersec:
            print("its time to drink water,type done to stop this alarm")
            musiconloop()
            log_now(f"drank water at")
            init_water=time()
        if time() - init_exercise >exercisesec:
            print("its time for some physical exercise,type done to stop this alarm ")
            musiconloop()
            log_now(f"done physical exercise at ")
            init_exercise=time()
        if time() - init_eye>eyesec:
            print(f"its time for some eye exercise,type done to stop this alarm")
            musiconloop()
            log_now(f"done eye exercise  at ")
            init_eye=time()





