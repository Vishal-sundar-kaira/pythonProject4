#os module is an operating system we can use it in multipurpose its an inbuilt module.it take care of every function performing.
#os can be used to rename file,find path,close,open file,etc..
import os
#print(dir(os))

#examples of os module uses.
print(os.getcwd())  # its an getcurrentworkingdirectory (place where its working).


#we can also change the place of os module working.
#os.chdir("c://")    #this is use to change place.
print(os.getcwd())
#f=open("harry excercise") #this file is in my python but showing error ,because we shifted our os module to c://

print(os.listdir())   # this give list of every folder in that programm if its c:// then recycle bin etc,if in python then alarm,iterable,etc...

#os.mkdir("This/that/how are you guys.")   # this is used to make an file in place where your module is located.
# with each slash it will go within like this will be folder in which there will be folder that in which there will be how are you.
#os.makedirs() we can use it also directly.
#os.rename("vishal diet","vishal health")#this is use to rename a file.

print(os.environ.get('path'))
print(os.path.join("c://","vishal health")) #this is use to join them but it did not get effect by any slashes.
print(os.path.exists("vishal health")) #it will show the programm exist or not.
print(os.path.isdir("c://"))  #can use to search same is in directory or not or in file or not by using isfile.
#Thus there are many types of os module use it when require.