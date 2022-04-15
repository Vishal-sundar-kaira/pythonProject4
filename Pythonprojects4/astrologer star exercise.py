print("astrology star")
num1=int(input("how much row you need: "))
bool_val=input("enter 1 or 0: ")
if bool_val=="1":
    for i in range(0,num1+1):
        print("*"*int(i))
elif bool_val=="0":
    for i in range(num1,0,-1):
        print("*"*int(i))

