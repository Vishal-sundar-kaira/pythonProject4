#The Next palindrome.
#palindrome is a string whose reverse is same as itself example is 616,mom,dad 4334.
#first ask user the number of input it like to give.
def palindrome(n):
    if n>10:
        while not is_palindrome(n):
            n=n+1
        return n
    else:
        return n

'''remember the part above it did not click me at first of creating both seperate fuction for ispalindrome and palindrome
 so imp was ispalindrome function making and last line of for range and while loop use .'''


def is_palindrome(n):
     return str(n)==str(n)[::-1]


number=int(input("NO of cases you like to input to find their next palindrome"))
list=[]
pallist=[]
for i in range(number):
     a=int(input("Type number whose next palindrome you like to see"))
     list.append(a)

for i in range(number):
    pallist.append(palindrome(list[i]))
print(pallist)