list=["virat","rohit","rahul","risabh","shami","bumrah"]
#we need to join all name with and normally we use for loop
'''for i in list:
    print(i,"and",end=" ")
print("are all cricketer")'''

#now we will do it with join function.
a=" and ".join(list)            #we can join list with anything.
print(a,"are all cricketer")


