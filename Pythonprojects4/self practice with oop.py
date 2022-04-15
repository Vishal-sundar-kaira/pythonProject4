class bank:
    def __init__(self,name,nominee,adhaar,mobile):
        self.name=name
        self.nominee=nominee
        self.adhaar=adhaar
        self.mobile=mobile
    def registration(self):
        return f"sbi bank registration form.\n" \
               f"candidate name is {self.name}\n " \
               f"{self.name} father name is {self.nominee}\n" \
               f"{self.name} adhaar number is {self.adhaar} mobile number is {self.mobile}\n" \
               f"{self.name} your sbi account is now activated you can now do deposits and after few days you can start your registration\n" \
               f"this form is created by official sbi which is led by vishal kaira \n" \
               f"THANKS FOR SUPPORTING SBI WE ASSURE YOU YOUR SECURITY\n"
a=bank(input("add your name"),input("add nominee name"),input("your adhaar number"),input("your mobile number"))
print(a.registration())
