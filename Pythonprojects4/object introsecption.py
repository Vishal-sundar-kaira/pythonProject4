#this is used to find object type.
class Empoyee:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
       # self.email=f"{self.name}@gmail.com"
    def explain(self):
        return f"my name is {self.name} and my gender is {self.gender} and my age is {self.age}"
    @property                              #property decorator is used to apply this fuction without(),becuase this made the fuction an argument or attribute.
    def email(self):
        if self.name==None:
            return "your email is deleted set it again with the help of setter"
        return f"{self.name}@gmail.com"
    @email.setter
    def email(self,str):                     #setter is used to set an any changes in function.
        self.name=str.split("@")[0]
    @email.deleter
    def email(self):                           #deleter is used to delete any attribute.
        self.name=None
vishal=Empoyee("vishal","male",19)
#vishal.name="kaira"
#print(vishal.email)
vishal.email="sahil@gmail.com"
print(vishal.email)
del vishal.email
print(vishal.email)
print(dir(vishal))
import inspect
print(inspect.getcomments(Empoyee))