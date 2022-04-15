'''def function1(a,b,c,d):
    print(a,b,c,d)                                 #in this way we use function but if we want to add one more name we
function1("vishal","sahil","bittu","abhishek")  '''   #have to do much changes in every line.

#what if you have to add many names use args
def funargs(normal,*args,**kwargs):                   #remember:we cant use normal after args.
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
list=("vishal","sahil","bittu","abhishek","vijay","rakesh")
normal="shiv ganga gang people"
kw={"vishal":"programmer","bittu":"web developer","sahil":"hotel manager","abhishek":"business man"}
funargs(normal,*list,**kw)
#*args help to store automatically in list way in tuple , it will store as an tuple and we can use it .

