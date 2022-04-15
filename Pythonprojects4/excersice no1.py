#excersise on age.
print("WELCOME TO VISHAL AGE AGENCY HERE YOU CAN GET INFORMATION ABOUT YOUR AGE ")
name=input("Enter your name")
a=int(input("Enter your age or your birth year"))
if a<0:
    print(f" {name} you are from different dimension we cant say anything about your age")
elif a<=999 and a<=150:
    print(f"{name} after {100-a} years you will be celebrating your 100th birthday")
elif a<=999 and a>150:
    print(f" {name} you should be the oldest person alive")
elif a>=1921 and a<=2021:
    print(f" {name} you will be celbrating your 100th birthday in year {a+100}")
elif a<1921:
    print(f"congrats {name} you are already above 100 years")
elif a==1921:
    print(f"congrats {name} this year is going to be your 100th year")
elif a>2021:
    print(f"sorry {name} I think so you are not born yet")
print("NOW YOU CAN ALSO CALCULATE YOUR AGE AT PARTICULAR YEAR.")
age=int(input("Enter your age"))
ageat=int(input("Enter year at which you want to know your age"))
if age<=200 and ageat>=2021-age:
    print(f" {name} you will be celebrating your {ageat-(2021-age)}th birthday  at {ageat}")
else:
    print(f" {name}  I think so you are the oldest person alive")

