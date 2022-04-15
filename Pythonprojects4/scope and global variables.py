
k=3     #its an global variable follows by every function
def function1(n):
    k=4       #this is local variable use by particular function in which it is
    print(n,"kaisan baa")
    print(k)  #if print is in under function then it will print local var i print is outside var it will show global var
function1(input())
print(k)
#now as per rule we cannot change global variable inside function to change it we need a special permission we use global
# global (var name which we want to change)
def function2(n):
    global k
    k=k+18
    print(n,"chalde beta tu idarse")
function2(input())
print(k)
