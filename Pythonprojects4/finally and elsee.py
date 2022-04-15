#else and finally with try and except.
#as we know we use try in which we add something and than we use except if try is invalid exception will come and program
# will continue rather it will not stop there with error.
f1=open("vishal diet")
try :
    f=open("vishal ")     #like this vishal.txt file doesn't exist in my python so it will not show error it will show exception.
except Exception as e:       #and with exception also we can print after it.
    print(e)
#we can also use other error if they came.
except EOFError as e:
    print("EoFError aa gya hai")
except IOError as e:
    print("IOError aa gya hai")

else:
    print("great your file is working.") # else is the statement which will only print if exception is not printing

                                          #if there is exception it will not print if file is correct except dont work then only else will print.

finally:                     #finally is something which should happen anyhow or print anyhow irrespective of try will work or except will work.
    f1.read()                 #finally will just print what it has given.it is mainly used to close file or clean up things.
print("how are you")
