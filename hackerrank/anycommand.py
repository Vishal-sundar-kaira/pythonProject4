if __name__ == '__main__':
    li=[]
    N = int(input("how many command"))
    for i in range(N):
        name,*line=input("command").split( )
        if name=="append":
            li.append(int(line[0]))
        elif name=="remove":
            li.remove(line[0])
        elif name=="pop":
            li.pop()
        elif name=="insert":
            li.insert(int(line[0]),int(line[1]))
        elif name=="sort":
            li.sort()
        elif name=="reverse":
            li.reverse()
        elif name=="print":
            i=print(li)
            li.clear()
#             12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

