#we need to pickle string in list form in our python and use it .
# import requests
# import pickle
# import json
# iris=open("iris.data")
# iris_read=iris.read()
# list=iris_read.split("\n")
# filename="justpickleit"
# fileopen=open(filename,'wb')
# finalpickle=pickle.dump(list,fileopen)
# print(finalpickle)

import pickle

with open("justpickleit", "rb") as f:
    print(pickle.load(f))
