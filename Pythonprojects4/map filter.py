#map:this function is use to apply any function in whole list at one time.
num=["2","3","33","58"] #we need to convert whole list in integer function.
'''for i in range(len(num)):
    num[i]=int(num[i])           #this is the way we can use to convert all list object in int by using for loop.

num[(3)]=num[(3)]+2
print(num[3])'''
#now we will use map.
'''numbers=list(map(int,num))      # in map (function you need to add,in which list you need to add this function)
numbers[(3)]=numbers[(3)]+2
print(numbers[3])'''
#practice
'''new=[34,45,45,68,34]
num=list(map(lambda x:x/10,new[:]))
print(num)
print(num)'''
#filte
'''filt_list=[1,2,3,4,5,6,6,7,8,9]
greater_than=list(filter(lambda x:x%2==0,filt_list))
print(greater_than)'''
'''Difference in map and filter is in map we say to do this changes in every object of list, example
divide everyone by 10.In filter we say to filter and 
gives us what we need example give us number more than 5,odd,even'''
#reduce
from functools import reduce
list1=[1,2,3,4,5,3]
#now we need to add every integer in list.
'''w=0
for i in list1:          #we can do using for loop
    w=w+i
print(w)'''
#using reduce
num=reduce(lambda x,y:x+y,list1)  #this fuction directly use add or substract.
print(num)
#map work on each object like to add 10 in everyone square of every object(x), but reduce do things link to other like add everyone(x,y)
#and filter always filter the object and give us what we need .


