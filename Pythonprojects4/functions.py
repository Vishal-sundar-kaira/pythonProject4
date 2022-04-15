# #types and use of function
# def function1():
#     """we can use input"""
#
# print(function1.__doc__)
#
# def function(x=int(input()),y=int(input()))
#
#     print("bhai tumhara jawab tehra",x+y)
# function()
# print("chalo bhai ye jawab to sahi dediya")
# def greet(name):
#     gr="hello\t" + name
#     return gr
# a=greet("vishal")
# print(a)
# def imp(a,b):
#     a1=a*b
#     return a1
#
# n1=imp(4,5)
# print(n1)
#try except exceptional handling python
#this is use when we dont want to come a invalid which will not show next line so for that we write except exception as e(we can write anything in palce
#of e and that only should use in print
print("enter your first number")
n1=input()
print("enter your second number")
n2=input()
try:
    print("the sum of your number is",int(n1)+int(n2))
except Exception as r:
    print(r)
print("get ready for next one")







