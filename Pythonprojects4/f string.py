#f string is used to add string in which f stand for fast as it is the fast way to add string
'''var1="vishal"
var2="so what can i do for you"            # its the one way to add in string
a="your name is %s %s"%(var1,var2)
print(a)'''
'''var1="sahil"
var2="are your ready"
a="so your name is {} {}"           #its the another way to add string but this all way will make things difficult
b=a.format(var1,var2)                #when their will be larger code.
print(b)'''
#so we use f string
import math
var1="bittu"
var2="are you ready to draw"
var3="it will be interesting"
a=f"so your name is {var1} {var2} {var3} {math.cos(90)}"
print(a)
print("so your name is",var1,var2,var3,math.cos(34))
#example
for key, value in kwargs.items():
    print(f"{key} is a {value}")






