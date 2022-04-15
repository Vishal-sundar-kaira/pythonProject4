#recurssion is function in function
#making a funtion for factorial

'''def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac=fac * (i+1)
        return fac
num=int(input("which number factorial you like to calculate\n"))
print(factorial_iterative(num))'''
#factorial using recurssive method
'''def factorial_recurssive(n):
    if n==1 or n==0:
        return 1                         #in this as you can see if i put 4 than that 4 will go to else n and then n-1 will be 3 which multiply
                                        # again by function of factorial 3 now n will be 3 and n-1 will be 2 and will now again give funtion of
    else:                               #2 and this will go on function on funtion till it reach 1 where it will be 1
        return n*factorial_recurssive(n-1)
num=int(input("enter number for factorial\n"))
print(factorial_recurssive(num))'''
#quiz
'''def fibonachi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)
num=int(input("enter number to calculate fibonachi\n"))
print(fibonachi(num))'''
#lymbda
#lymbda is one liner function use to write def function in short way
def add(a,b):
    return a+b
print(add(6,4))
#using lambda
add=lambda a,b:a+b
print(add(6,4))
#using sort function(put everything in ascending order)
def a_first(a):
    return a[1]
a=[[1,18],[4,26],[3,11]]
a.sort(key=a_first)        #key is use to define function criteria
print(a)
#using lambda

a=[[1,18],[4,26],[3,11]]         #lambda means ek aisa function banado jo
a.sort(key=lambda a:a[1])        #key is use to define function criteria
print(a)


