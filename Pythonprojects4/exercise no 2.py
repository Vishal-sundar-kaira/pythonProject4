#excersice of divide apple.
n= int(input("Enter numbers of  apple available"))
min=int(input("Enter minimum number of student are there"))
max=int(input("Enter maximum number of student are there"))
print("apple can be distribute to....")
for i in range(min,max+1):
    if n%i==0:
        print(f"{i} numbers of students are eligible for getting apple")
    else:
        print(f"{i} numbers of students are not eligible for apples")

for i in range(min,max+1):
    a=n%i
    if a==0:
        print(f" for {i} students congrats you can share this apple in equal amount")
    elif a<=i/2:
        print(f" for {i} we want you to romve {a} apples ")
    elif a>i/2:
        print(f" for {i} we want you to add {i-a} apples ")
