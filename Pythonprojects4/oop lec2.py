#we cannot change class variable by instance variable.
class Employee:
    no_of_leaves=8
    pass
harry=Employee()
vishal=Employee()

harry.name="harry"
harry.salary=355
harry.role="director"
vishal.name="vishal"
vishal.salary=3554
vishal.role="hero"     #we came to conclusion that if we change the vishal or harry particular variable it will make only change in them
vishal.no_of_leaves=9      #a new variable will generate on them that change will not effect others but if i make change in employee var of class
print(Employee.no_of_leaves)                         # it will make change in all var,nobody can change class var except class itself employee.
print(Employee.__dict__)
Employee.no_of_leaves=3

print(harry.no_of_leaves)