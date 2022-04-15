#faulty calculator
print("number 1")
n1=int(input())
print("number 2")
n2=int(input())
print("enter your operator")
op=(input())
if n1==45 and n2==3 and op=="*":
    print("555")
elif n1==56 and n2==9 and op=="+":
    print("77")
elif n1==56 and n2==6 and op=="/":
    print("4")
elif op=="+":
    print(n1+n2)
elif op=="*":
    print(n1*n2)
elif op=="-":
    print(n1-n2)
elif op=="/":
    print(n1/n2)


