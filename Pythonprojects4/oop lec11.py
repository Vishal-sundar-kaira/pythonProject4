#operator overloading and dunder method.
class Employee:
    no_of_leaves=8
    def __init__(self,aname, asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetail(self):
        return f"Name is {self.name} salary is {self.salary} role is {self.role}"
    @classmethod
    def change_leaves(cls,new_leaves):         #with  the help of class method we can make chanages in class variable with instance variable,as it does not take
        cls.no_of_leaves=new_leaves
    def __add__(self, other):                #this is one of the dunder method which use __ and with this we done the operator overloading of add.
        return self.salary+other.salary
    def __repr__(self):
        return  f"Name is {self.name} salary is {self.salary} role is {self.role}"      #repr and str are another dunder method it print without calling printdetail
    def __str__(self):                                                                  #and also str will always print first if both are there,but if you need repr
        return  f" My Name is {self.name} salary is {self.salary} role is {self.role}"  #you can call it print(repr(a)).
    def __contains__(self, item):
        return f"{self.name}{item.name}"

a=Employee("bittu",20,"dancer")
b=Employee("vishal",50,"programmer")
print(a)