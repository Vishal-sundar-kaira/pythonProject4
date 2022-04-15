#generator is an iterator(which repeat things in loop) which give us only vlaue at a time not while loop give all value at one time by iterating
# but generator give one by one as we typr __next__() and then another with another next
#we can use this things if there are millions of file and we dont want all of them to come our system we will set generator on how to come and will call it
# one by one using next(). Yield is an generator used instead of return.  string is iterable and int are not.
def gen(n):
    for i in range(n):
        yield i
q=gen(5)
print(q.__next__())
print(q.__next__())
#quiz

def factorial(a):
    if a==0 or a==1:
        return 1
    sum=a
    sum=sum*(factorial(a-1))
    return sum

def gen_fact(n):
    for i in range(n):
      yield print(factorial(i))
g=gen_fact(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())



