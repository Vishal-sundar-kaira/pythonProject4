
def swap_case(s):
    lis=[]
    for i in range(len(s)):
        s=str(s)
        a=s[i]
        c=a.capitalize()
        if a==c:
            l=a.lower()
            lis.append(l)
            
        elif a!=c:
            ca=a.capitalize()
            lis.append(ca)
    j="".join(lis)

    return j

if __name__ == '__main__':
    s=input("string")
    print(swap_case(s))
#There are already inbuilt function of swap_case
        