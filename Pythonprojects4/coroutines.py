#coroutines is little bit like an chaching which will save our time .
def searcher():
    import time
    book="this is an book of vishal kaira"
    time.sleep(4)# think this as it take 4 second task to read any long files or books.
    while True:
         text=(yield)#this make the function an coroutine and the searcher information will get store in this yield so
                     #next time if we call the fuction we dont have to wait 4 second it will start directly from while loop.
         if text in book:
             print("your text is in book")
         if text not in book:
             print("your text is not in book")
search=searcher()
next(search)             #in this way we fully use it as an coroutines.This will run whole starting fuction of time.
search.send("vishal")    # in this way we give them value to search which will get store in text next time.
input("press any key")
search.send("vishal and")
search.close()# in this way we can close this coroutines and we can start it again by starting from search of 13 line.
#IN this way we can use it infinite time to find text from a big file which is taking 4 second at starting but at
#second time it will not take any time.

#quiz
def letsee():
    import time
    selected=("vishal","sahil","bittu","abhishek","rohan","aditya","sunidhi","anjali","bharti","bhagyashree","rohit","ajay","vijay","rakhi","subham","sagar")
    time.sleep(5)
    while True:
        text=(yield)
        if text in selected:
            print("congratulation you are selected")
        else:
            print("your are not in this race")
search=letsee()
n = input("input your name letsee you got selected or you are  not in race")
next(search)
search.send(n)
a=input("enter name")
search.send(a)
b=input("enter name")
search.send(b)

