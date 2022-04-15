if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b=[i for i in a if i[0]!=a[0][0]]
    c=[j for j in b if j[0]==b[0][0]]
    c.sort(key=lambda x:x[1])   #use to sort second index.
    for k in range(len(c)):
        print(c[k][1])


        
    
        
    



    
   
