#inheritance.
#single inheritance.
#in inheritance we copy like dna we copy other fuctions cls
#we make more class to add extra things on particular instance variabels but it will perform everthing of first class by just putting class 1 name in argument.

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
    @staticmethod
    def printgood(string):
        print(string,"is a very good boy")    #directly we can print aything with the help of staticmethod.
        return "done"
class programmer(Employee):
    def __init__(self,aname,asalary,arole,language):          #now we added one more agrumnent languange by using init function and rest is same of employee.
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=language

    def printprog(self):
        return  f"The programmer Name is {self.name} salary is {self.salary} role is {self.role}and language he knows{self.language}"


harry=Employee("harry",477,"director")
vishal=Employee("vishal",399,"hero")
sahil=programmer("sahil",4999,"producer",("python","java","c++","html"))

aditya=Employee.from_str("aditya-4888-spotboy")
vishal.change_leaves(44)

print(vishal.printdetail())
print(harry.printdetail())
print(sahil.printprog())
print(sahil.printdetail())
