def getdate():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        print("whose health system you want to log")
        print("1.vishal,2.harry")
        n=int(input())
        if n==1:
            print("which system you want to log of vishal,1.exercise,2.diet")
            c=int(input())
            if c==1:
                num1=input("write exercise name")
                f=open("vishal exercise","a")
                print(f.write(str((getdate()))+num1 +"\n"))
            elif c==2:
                num1 = input("write diet name")
                f=open("vishal diet","a")
                print(f.write(str(getdate())+ num1 +"\n"))
        if n==2:
            print("which system you want to log of harry,1.exercise,2.diet")
            c=int(input())
            if c==1:
                num1 =input("write exerxise name")
                f=open("harry exercise","a")
                print(f.write(str(getdate()) + num1 + "\n"))
            elif c==2:
                num1 = input("write diet name")
                f=open("harry diet","a")
                print(f.write(str(getdate()) + num1 + "\n"))
    else:
        print("invalid")
        return take(k)

def retrive(k):
    if k==1:
        print("whose health system you want to retrive")
        print("1.vishal,2.harry")
        n=int(input())
        if n==1:
            print("which system you want to retrive of vishal,1.exercise,2.diet")
            c=int(input())
            if c==1:
                f = open("vishal exercise")
                print(f.read())
                for i in f:
                    print(i," ")
            elif c==2:
                f = open("vishal diet")
                print(f.read())
                for i in f:
                    print(i," ")
        elif n==2:
            print("which system you want to retrive of harry,1.exercise,2.diet")
            c=int(input())
            if c == 1:
                f = open("harry exercise")
                print(f.read())
                for i in f:
                    print(i, " ")
            elif c == 2:
                f = open("harry diet")
                print(f.read())
                for i in f:
                    print(i, " ")
    else:
        print("invalid")
        return retrive(k)
print("welcome to vishal health system type 1.If you want to log 2.If you want to retrive")
a=int(input())
if a==1:
    b=int(input("press 1 to start"))
    take(b)
elif a==2:
    b=int(input("press 1 to start"))
    retrive(b)










