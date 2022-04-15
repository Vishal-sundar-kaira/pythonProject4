a=input("Enter your name")
if a.isnumeric():
    raise Exception("numbers are not allowed")
b=int(input("how much do you earn"))
if b==0:
    raise ZeroDivisionError("b is 0 so it is stopping the programm")#this are different type of error in raise.
print(f"hello {a}")
#assume there is 1000 hours coding after this and then it will show the result of input a and if it is error it will show
#error after this much time but we want to detect error in starting so for that we use raise .(it give error just after input without starting programming.)
c=input("Enter your name")
try:
    print(a)            #as we can see we printed "a" which is not there so it will print exception.
except Exception as e:
    if c=="vishal":       #if name is vishal it will show this type error.
        raise ValueError("vishal namak prani idar allowed nhi he")
    print("your name is handled") # if name is not vishal it will print this exception.
#In this way there are many types of error with raise.