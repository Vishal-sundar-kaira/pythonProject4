'''f=open("vishal file1","r")
content=f.read()
print(content)                                 (this is for reading file)
for line in f:
     print(line,end="")
print(f.readline())        can see line by line
print(f.readlines())
        f.close()             can see in list'''

#now lets learn to write in file
'''f=open("vishal file1","w")                                  now in this we can write anything in file but previous one will not be there
content=f.write("vishal also love to play cricket")
print(content)
f.close()'''
#now lets learn to add in files using append
f=open("vishal file1","r+")
content=f.read()
print(content)
f.write("favourite dish of vishal is pav bhaji")
f.close()