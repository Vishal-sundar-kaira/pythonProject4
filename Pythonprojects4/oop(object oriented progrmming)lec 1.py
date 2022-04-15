'''now lets learn about oop(object oriented programming.
python support many ways to function oop is one of the way(good way) so we can do same function with other way,but now we will focus on oop
1.classes-Template(it is same as template in this we need to assign permanent thing which will applicable for all,we dont need to repeat things.
for eg:-in bank if you withdraw money they give us receipt in which they only add your name and amount and rest other things
like your age and she had taken__this much amount this will automatically print if we assign then in class
2.object-Instance of the class (like she had taken this much is classes that are already written then we write amount and we get our result ready
 that is an object.'''

class Students:
    pass
harry=Students()              #they are two instans of students object.
vishal=Students()             #they both are different.
vishal.marks=23
harry.marks=84                  #now this are instans variables.
vishal.salary=39999
harry.salary=338398

print(harry.marks,vishal.marks)   #printed instans varialbe

