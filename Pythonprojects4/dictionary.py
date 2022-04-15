'''d1={"vishal":"cricket","sahil":"hotel","bittu":"artist","absek":"business","life":{"health":"exercise","wealth":"career","love":"honest"}}
d1["rohan"]="beatboxer"
d2=d1.copy()
del d2["rohan"]
d3=d2
print(d3["vishal"])'''
# dictionary={"python":"A coding course use to make an app and web","patanjali":"India fastest growing company,started by ramdeobaba","heart":"An important organ of a body,use to suppply blood","marathon":"Running competition"}
#
# print("enter your word")
# n1=input()
#print("meaning :",dictionary[n1])
dictionary={}
i=0
while(i<1):
        name=input("your name")
        passion=input("your passion")

        dictionary.update({name:passion})
        print(dictionary)
        a = input("what you want to know")
        print(dictionary.get(a))

