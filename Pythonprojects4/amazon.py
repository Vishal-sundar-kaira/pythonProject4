#its an amazon sale game.
print("Welcome to refun website")
print("Here you can add your products for sale and also buy products for yourself")
a = input("enter your name")
class refun:
    def __init__(self,a):
        self.items={}
        self.name=a
    def add_item(self):
        print("which item you like to add")
        itemm=input("Enter your item name")
        pricee=input("Enter the price at which you like to sell this item")
        self.items.update({itemm:pricee})
        print(f"Thanks {self.name} for adding your product {itemm} in our list")
    def display_items(self):
        print("which item you like to buy")
        print(self.items)
        item_name=input("Enter your item name you like to buy")
        if item_name in self.items:
            while(True):
                moneyy = self.items[item_name]
                money = input("enter money ")
                if money==moneyy:
                    print(f"Thank you soo much mam for shopping {item_name}")
                    break
                else:
                    print("sorry mam your money is not correct try again")
                    continue
        else:
            print("sorry this item is not present here")

costumer_book=refun(a)
costumer_cloth=refun(a)
costumer_games=refun(a)
costumer_furniture=refun(a)
if __name__ == '__main__':
    while(True):
        b =int(input(f"Hii {a} what can we do for you 1.add your item on sale,2.display choices of products as per your choices"))
        if b==1:
            genre=int(input("In which genre you need to go 1.books,2.cloth,3.games,4.furniture"))
            if genre == 1:
                print(costumer_book.add_item())
            elif genre == 2:
                print(costumer_cloth.add_item())
            elif genre == 3:
                print(costumer_games.add_item())
            elif genre == 4:
                print(costumer_furniture.add_item())
            else:
                print("Try again your character is incorrect")
        elif b==2:
            genre = int(input("In which genre you need to go 1.books,2.cloth,3.games,4.furniture"))
            if genre == 1:
                print(costumer_book.display_items())
            elif genre == 2:
                print(costumer_cloth.display_items())
            elif genre == 3:
                print(costumer_games.display_items())
            elif genre == 4:
                print(costumer_furniture.display_items())
            else:
                print("try again your character is incorrect")
        else:
            print("something went wrong try again type 1 or 2")





