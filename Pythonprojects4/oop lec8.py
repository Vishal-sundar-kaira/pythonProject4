#multilevel inheritance.
class Dad:
    basketball="dad was great in basektball"
class son(Dad):
    carrom="son is also good in carrom"
class grandson(son):
    cricket="grandson is very good in  cricket"
print(grandson.carrom)
#This is mutilevel inheritance in which we can get every quality in grandson of son and dad,it will first find attribute in itself if its not there
#it will go to the class given in argument(son) and then dad.

#exercise.
class electronic_gadget:
    quality1="its an gadget which is portable pocket gadget or fix gadget and many more"
class pocket_gadget(electronic_gadget):
    quality2="its an gadget which is easily portable , it include phone,digital watch,bluetooth,etc"
class phone(pocket_gadget):
    quality3=f"its is a very addictive gadget,we can use it for good purpose also it is easily portable"
print(electronic_gadget.quality)
