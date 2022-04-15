#class method.
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
        cls.no_of_leaves=new_leaves              #self it take cls.
    @classmethod
    def from_str(cls,string):
         #param= string.split("-")                  #we can also make string split in three argument which we need name,salary,role with string.split
         #return cls(param[0],param[1],param[2])  #strin.split split with - and then we use *args which store them as a list.
    #alternative method using args
         return cls(*string.split("-"))




harry=Employee("harry",477,"director")
vishal=Employee("vishal",399,"hero")
sahil=Employee("sahil",4999,"producer")
aditya=Employee.from_str("aditya-4888-spotboy")
vishal.change_leaves(44)

print(vishal.printdetail())
print(harry.printdetail())
print(sahil.printdetail())
print(aditya.no_of_leaves)
print(aditya.printdetail())