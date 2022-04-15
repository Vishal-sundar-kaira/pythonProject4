#jumble the name.
#In this we need to take names as an input and then jumble that names surname.
import random
namee=int(input("How many names you like to input."))
nam=[]
sur=[]
for i in range(namee):
    name=input("Enter name of the person whose result you like to see")
    a=name.split(" ")
    nam.append(a[0])
    sur.append(a[1])
for i in range(namee):
    b=random.choice(nam)
    c=random.choice(sur)
    print(f"{b} {c}")
    nam.remove(b)
    sur.remove(c)


