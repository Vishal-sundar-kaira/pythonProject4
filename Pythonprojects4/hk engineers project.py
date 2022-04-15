#two wheller and three wheeler products showroom.
print("Hello welcome to s.p.s.e(save plastic save environmnet)")
print("Here you can giveaway your plastic or you can buy beautiful products made from plastic or you can contribute some plastic waste in your home for further recycle")


class Startup:
    def __init__(self,name,plastic):
        self.plastic=plastic
        self.name=name
    def buy_plastic(self):
        print(self.plastic)
        pname=input(f" {self.name} name the product you want to buy")
        int(input(f" {self.name} pay the price for it as mentioned"))
        try:
         self.plastic.pop(pname)
        except Exception as e:
            print(e)
        print("Thanks for buying your product will get deliver by tomorrow.")
    def give_plasticsale(self):
        print(self.plastic)
        sname=input(f" {self.name} name of your product which you want to put on sale")
        price=input("price at which you want to put it in sale")
        self.plastic.update({sname:price})
        print(f" {self.name} Thanks for your products,we hope you will do more for our environment")
    def give_plastic(self,weight):
        print(self.plastic)
        print(f" {self.name} thank you soo much for providing us {weight} gm plastic,we will make sure to recycle it in something new")
plastic={"hand bag":45}
if __name__ == '__main__':
    while (True):

        n = input("Enter your name")
        a = int(input("what do you want to do 1.buy plastic products,2.give plastic for sale,3.give plastic products for recycle"))

        vishalkaira = Startup(n, plastic)

        if a==1:
            print(vishalkaira.buy_plastic())
        elif a==2:
            print(vishalkaira.give_plasticsale())
        elif a==3:
            weight = (int(input("firstly thank you soo much for contributing to our environment, how much gram plastic are you providing us")))
            print(vishalkaira.give_plastic(weight))
