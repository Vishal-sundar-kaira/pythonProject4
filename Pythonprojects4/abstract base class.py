#abstract method means every class should contain this function given in  abstract method.
#like in this every class inhireted by shape should compulslary contain printarea which is used in abstract method
#this method is used to force user to define this fuction compulsary if you are inheritating that class.
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod              #this is how it is used.
    def printarea(self):
        return f"hii how are you"
class rectangle(shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=4
        self.breadth=6
    def formula(self):
       return self.length*self.breadth
    def printarea(self):
        return"aur kasian baa"
a=rectangle()
print(a.formula())

