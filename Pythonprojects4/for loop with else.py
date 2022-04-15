#now we are going to use for loop with else statement.
#else statement work only after for loop is compelted properly.
khaana=["daal","bhaat","roti","sabji"]
n=input("konsa khaana khaaneko pasand karoge")
for item in khaana:
    if item==n:
        print("thanks for buying")
        break

#like this only if for loop work properly it will not come if item is not in for loop it will print else statement.
else:
    print("ye khaana yaha nhi milta mere bhai, kuch aur try kar")

