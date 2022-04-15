#json=java script object notation.
#it is specially used to convert python format to java or java to python.
#this will help everytime we import files from online to read it will convert them in format of python to play using load
#and if you want the python file to be used in outside online or in java it will convert using dumps. there are both load and loads , dump and dumps
#s just means we need that file in string format in without s you can directly  give file.
import json
data='{"vishal":"programmer","college":"thadomal","course":"computer engineering"}'
parsed=json.loads(data)    #this help to parsed(simplify and in best way) the function.
print(parsed['vishal'])   #noramlly we cant call vishal only but we can after parsed.
#Loads help to convert java dictionary in python.

data2={"vishal":"programmer","college":("thadomal","thakur","kj soumiya"),"course":["computer engineering","IT","AIDS"],"isbad":False}
jscomp=json.dumps(data2) #this help to convert python dict in java dict.
print(jscomp)
dataa=["vishal","sahil",True]
name=json.dumps(dataa,sort_keys=False)
  #sort key is used to order dict in alphabetic order.
print(name)


f=open("vishal exercise")
data3=json.load(f)  #used to read from file but it should be in dictionary format.
print(data3)
