#first game of my life stome paper and scissor
def selction(s):
      if s==1:
            print("so your choice is stone")
      elif s==2:
            print("so your choice is paper")
      elif s==3:
            print("so your choice is scissor")
      else:
            print("your data is invalid")

print("stone paper and scissor game by vishal.")
print("rules:you have to select any option between stone paper and scissor and computer will automatically select any one.\n"
      "if you won you got the point,there will be 10 rounds")
print("lets start the game\n")
tp1=input("press enter")
print("type your name")
username=input()
i=0
u=0
c=0
d=0
while(i<10):
      n=int(input("what you like to choose between 1.stone 2.paper 3.scissor"))
      selction(n)
      print("now computer will choose randomly")
      input("press enter")
      import random
      list=("stone","paper","scissor")
      a=random.choice(list)
      print("computer choice is",a)
      print("result")
      input("press enter")
      if n==1:
            i=i+1
            if a=="stone":
                  d=d+1
                  print("nobody gets the point")
                  print(username, u, "computer", c)
                  print("total rounds remainig",10-i)

            elif a=="paper":
                  c=c+1
                  print("this point goes to computer")
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)

            elif a=="scissor":
                  u=u+1
                  print("this point goes to",username)
            print(username, u, "computer", c)
            print("total rounds remainig", 10 - i)

      elif n==2:
            i=i+1
            if a == "stone":
                  u=u+1
                  print("this point goes to ",username)
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)


            elif a == "paper":
                  d=d+1
                  print("nobody gets the point")
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)

            elif a == "scissor":
                  c=c+1
                  print("this point goes to computer")
            print(username, u, "computer", c)
            print("total rounds remainig", 10 - i)


      elif n==3:
            i=i+1
            if a == "stone":
                  c=c+1
                  print("this point goes to computer")
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)

            elif a == "paper":
                  u=u+1
                  print("this point goes to",username)
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)

            elif a == "scissor":
                  d=d+1
                  print("nobody gets the point")
                  print(username, u, "computer", c)
                  print("total rounds remainig", 10 - i)


if u>c:
      print("winner is",username)
elif u<c:
      print("winner is computer")











