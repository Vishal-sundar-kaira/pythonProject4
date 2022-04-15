'''f=open("vishal file1","r")
print(f.readline())
print(f.seek(10))    #its use to restart the things like for another readline it will start to read from restart where seek say
print(f.readline())
print(f.tell())        #its say us upto which character we had print in read line
f.close()'''
#new way to write open and close whole things same as it done in 1 2 line and it also close it
with open("vishal file1") as f:
    print(f.readlines())
f=open("vishal file1","r")
print(f.readline())
