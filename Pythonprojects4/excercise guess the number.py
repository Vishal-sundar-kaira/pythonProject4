n=48
i=0
while(i<9):
    n1=int(input("guess the number"))
    i = i + 1
    if n1>n:
        print("choose less value than this",9-i,"guesses left")
        continue
    elif n1<n:
        print("choose bigger value than this",9-i,"guesses left")
        continue
    elif n1==n:
        print("congratulation you won in",i,"guess")
        i=i+1
        break
    else:
         print("game over")
         break



