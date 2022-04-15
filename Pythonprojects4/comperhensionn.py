#make list,dictionary,generators,sets in one line.this method use to make list or dict or generator or sets shortly.
#for eg we need to make a list of number divisible by 3 we can make with normal method.
list=[]
for i in range(100):
    if i%3==0:
        list.append(i)
print(list)
#now we will do it with comperhension method.
a=[i for i in range(100) if i%3==0]   #list comperhension method.we use square bracket[]
print(a)
#dictionary comperhension method. we use curly bracket with key and value.
item=("vishal","sahil","bittu","Abhishek")
#dict={1:item[0],2:item[1],3:item[2]} like this we cant add millions object in list.
dict={i:f"item{i}"for i in range(100) }   #so we use this method.
print(dict)
dict={value:key for key,value in dict.items()}  # In this way we can also reverse the key and value place.
print(dict)
#comperhension for sets.we use curly bracket.
dresses={dress for dress in {"dress 1","dress 2","dress 2"}}  #sets dont repeat item
print(dresses)
#comperhension for generators.it use perenthesis()
gen=(i for i in range(100) if i%2==0)
print(gen.__next__())
print(gen.__next__())