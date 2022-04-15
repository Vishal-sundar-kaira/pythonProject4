#reverse the list by using three methods.
foods=[]
#first reverese using any inbuilt method.
print("welcome sir to our vishal restaurant,we will serve you the best")
print("Here you can order any five dish of your choice")
for i in range(5):
    print(f"your dish no {i+1}")
    list=input()
    foods.append(list)
print(foods)
print("as per reverse calories")
def inbuilt():
    foods.reverse()
    print(foods)
#now reverse using -1(string slicing)method.
def split():
    lsplit=foods[::-1]
    print(lsplit)
def exchange():
    reverse=foods[:]
    a=len(foods)
    for i in range(len(reverse)//2):
        reverse[i],reverse[a-i-1]=reverse[a-i-1],reverse[i]
    print(reverse)
select=int(input("which method you like to use 1.inbuilt,2.split,3.exchange"))
if select==1:
    print(inbuilt())
elif select==2:
    print(split())
elif select==3:
    print(exchange())
