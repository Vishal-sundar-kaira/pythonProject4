#self and init(constructor)
class Employee:
    no_of_leaves=8
    def __init__(self,aname, asalary,arole):
        self.name=aname                       #this is called constructor all argument which cant be stored in employee now came to init and in this we dont need
        self.salary=asalary                   #to write again and again harry., vishal, we just need to give name later.
        self.role=arole

    def printdetail(self):     # in self the person name will come whose detail you need ,we use this to make our work more fast less repetetive
        return f"Name is {self.name} salary is {self.salary} role is {self.role}"# later we just need to print this function with name in every self name will come.


harry=Employee("harry",477,"director")
vishal=Employee("vishal",399,"hero")
sahil=Employee("sahil",4999,"producer")
aditya=Employee("aditya",4888,"spotboy")


print(vishal.printdetail())
print(harry.printdetail())
print(sahil.printdetail())
print(sahil.no_of_leaves)
print(vishal.name)
# harry.name="harry"
# harry.salary=355
# harry.role="director"
# vishal.name="vishal"
# vishal.salary=3554
# vishal.role="hero"
# print(harry.printdetail())
# now we don't need to write that string again and again we just need to make vishal.salary and print vishal.printdetail
#but if we need more name we had to write many time thier name.salary,role.for that we use contractor with fuction init,we cant write arguments in
#instant(employee)so we use init

