print(" welcome to genie library")

class library:

    def __init__(self,library_name,book):
        self.library=library_name
        self.books=book

    def book_display(self):
        print(self.books)
    def lend_book(self,name,lendbook):
        if lendbook not in books_lended.keys() and lendbook  in books:
           books_lended.update({lendbook:name})
           print(f"Thanks for buying book {name}")
           print(books_lended)
        elif lendbook in books_lended.keys():
           print(f"sorry this book is already taken by {books_lended[lendbook]}")
        if lendbook not in books:
            print("we dont have this book")

    def add_book(self,new_book):
        self.books.append(new_book)
        print("your new book is added to our genie land")

    def return_book(self,bookreturn,name):
        if bookreturn in books_lended:
            books_lended.pop(bookreturn)
            print(f"Thanks {name} for reading this book")
        else:
            print("this book is not our")
books = ["Metamorphosis", "subtle art of not giving fuck", "Think and grow rich", "Uzumaki",
                     "power of subconscious mind"]
books_lended={}
if __name__=="__main__":
    while(True):
        z = input("enter your name master\n")
        vishal_library = library("genie", books)

        A=int(input("your which wish you want me to grant master , type 1.display books , 2.lend book , 3.add book , 4.return book \n"))
        if A==1:
            print(vishal_library.book_display())
        elif A==2:
            vishal_library.book_display()
            l=input(f"which book can this genie lend you master {z}")
            vishal_library.lend_book(z,l)
        elif A==3:
            n=input(f"which book you like to add master {z}")
            vishal_library.add_book(n)
        elif A==4:
            R=input(f"which book you like to return master {z}")
            vishal_library.return_book(R,z)




