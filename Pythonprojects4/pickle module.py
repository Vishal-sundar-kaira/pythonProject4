#Pickle is use to store list for eg we get an list after 5 minutes of working and if we need that list again and again
# We can store that list using pickle and use it as per our convinence.
import pickle
# games=["coc","pubg","squid game","marvel game"]
# file="game_store"
# objfile=open(file,'wb')            #This is the way to pickle any list.
# pickle.dump(games,objfile)

#Now we will learn the way to unpickle list from file.
file="game_store"
objfile=open(file,'rb')
mygames=pickle.load(objfile)
print(mygames)
