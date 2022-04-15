def mutate_string(string, position, character):
    lis=[]
    for i in range(len(string)):
        a=string[i]
        lis.append(a)
    lis.pop(position)#Remember to remove from index use pop
    
    j="".join(lis[:position])#join method
    j1="".join(lis[position:])
    final=j+(character)+j1 
    return final

if __name__ == '__main__':
    s = input()
    i, c = input().split(" ")
    s_new = mutate_string(s, int(i), c)
    print(s_new)