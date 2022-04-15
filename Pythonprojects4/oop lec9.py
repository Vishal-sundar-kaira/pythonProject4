''' there are three types of variable
1.public:- IN this the variable is allow to use by anybody or anyone can call this variable.
2.protected:-In this the variable can be used by only that particular class and their subclasses(for which we use underscore(_)
3.private:-In this the variable can only be used by that particular class(for which we use double underscore(_) and also we call it differently.'''
class Dad:
    basketball="dad was great in basektball"
    var1="aur kaisan baa"
    _var2="sab badhiya tum batao"
    __var3="are ham bhi badhiya chalte he phir bye"
class son(Dad):
    carrom="son is also good in carrom"
class grandson(son):
    cricket="grandson is very good in  cricket"
print(grandson.carrom)
print(son.var1)
print(son._var2)
print(Dad._Dad__var3)
