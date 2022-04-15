#overriding and super().
#overriding is the one we copy same attribute or instance on other class inherit by them.

class A:
    classvar1="i am class var 1 of class A"
    def __init__(self):
        self.classvar1="I am inside class A constructor,class var1"
        self.var1="i am an instance var 1 of class A constructor"
class B(A):
    classvar1="i am a class var 1 of class B "
    def __init__(self):                                   #here we had override same thing from class A so this is call overriding.
        super().__init__()                                 #remember:if we call any attribute with print outside class from this class it will first look within
        self.classvar1="I am inside class B constructor,class var1"#first it will always find in instance if its not there it will not call normal attribute direct
        self.var1="I am an instance of class B var 1"         #It will go to the class inherited there it will look in instance if its there it will call it if not
a=A()                                                       #then it will come again to its own class and search for normal attribute and then go for inherited class
b=B()                                                       #normal attribute,thus it will always first search in instance (this condition is without overriding).
print(b.classvar1)
'''if there is an overriding then it will completly forget about inherited class so if any attribute get call after looking within for instance it will not go
for inherited class instance it will give its own normal attribute.so,for moving to inherited class instance we need to use super function it will make it move there
and also remember if super is called first and its own instance are afterward so it will first go in super and then come again within and then again it will find
instance than it will print its own instance and if super is written later then it will only print instance of super.
'''
#daimond shape problem:
class A:
    def met(self):
        print("this is a method from classA")
class B(A):
    def met(self):
        print("this is a method from classB")
class C(A):
    pass
class D(B,C):
    pass
a=A()
b=B()
c=C()
d=D()
d.met()