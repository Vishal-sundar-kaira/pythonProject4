'''list=[["vishal",7],["sahil",24],["absek",17],["bittu",12]]
dict=dict(list)
print(dict)

for item,loop in list:
    print(item,"birthdate is ",loop)'''
list=["vishal","sahil",345,455,234]
for item in list:
    if str(item).isnumeric() and item <400:
     print(item)

#while loop
#i=0
#while(i<100)
'''for i in range(100):
    if i<30:
        continue
        i = i + 10
    print(i)
    if i==50:
        break
        i=i+10'''
#quiz


for i in range(5):
    n1=int(input("enter your number\n"))
    if n1>100:
        i=i+1
        print("greater than actual value and your attempt left is",5-i)
        continue

    elif n1<100:
        i=i+1
        print("less than actual  and your attempt left is",5-i)
        continue
    else:
        print("congratulation")
        break



