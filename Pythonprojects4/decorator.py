# def function1():
#     print("yo kaisan baa")
#
# func2=function1()
# del function1           #after deleting fuction 1 than also func2 show print as it already get assign in func2
# func2

 #in decorator we learn fuction in function where function can also be used as argument
def funcret(num):
     if num==1:
         return print
     if num==0:
         return sum
print(funcret(1))
#now lets use function as argument
#in this as we can make one function and try many function at one time in them

#@function1 means this function where @ is applied now lie in the function1 function.
def executor(func1):
    def nowsec():
        print("executing")
        func1()
        print("executed")
    return nowsec


@executor
def func():
    print("aur kaisan baa")

func()
@executor
def func2():
        print("let's play football")
func2()
@executor
def halwa():
    print("wahh bete mauj kardi")
halwa()



