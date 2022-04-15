#enumerate is just to make our life more simpler,its an short way to perform

list=["aalo","batata","kaanda","bhajia"]
'''i=1
for item in list:
    if i%2 is not 0:
        print(f" please bring {item}")
        i+=1'''
#enumerate way
for index,item in enumerate(list):
    if index % 2!=0:                       #now i dont need to write again and again for i it automatically has index in it.
        print(f" vishal seth please bring {item}")