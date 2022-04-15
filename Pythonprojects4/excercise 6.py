#Rohan Das is  a fraud.
#we need to make a function made by a rohan das in which it will show the table of given number in which it will randomly make any 1 table wrong
#and also need to make an fuction which detect wrong table made by rohan das.
import random
def table(n):
    i=0
    for i in range(10):
        a=n*i
        tablist.append(a)
    cho=random.choice(tablist)
    for i in range(len(tablist)):
        if tablist[i]==cho:
            tablist[i]=cho+2
def iscorrect(n):
    for i in range(len(tablist)):
        if tablist[i]!=n*i:
            print(f"{tablist[i]} is an wrong calculation its answer should be {tablist[i]-2}")
print("Rohan das table")
num=int(input("whose table you like to calculate?"))
tablist=[]
table(num)
print(tablist)
print(iscorrect(num))
print("Rohan das is fooling us by making an faulty calculator but you can use it now as it will detect what is wrong and will give you right answer")