# we use if_name_==_main_ so that if we want to import this tutmain1 file to tutmain 2 the other already used content will not come.
def vishal(string):
    print(f"are you ready to turn up tonight {string}")
def addition(a,b):
    return a+b+5
print("kaisan baa",__name__)                  # in this name value will be main in this file but in other file where it is imported will show tutmain1.
if __name__ == '__main__':                    #this will allowed this print only to work here it will not paste in other
    print(vishal("remember the name"))        #where tutmain1 is import and only function will work.
    print(addition(4,5))