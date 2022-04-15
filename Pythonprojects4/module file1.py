import flask
print(flask)
import sys           #fuction tells us the path at which python find module.
print(sys.path)
# as we can see the path it start to find module first in itself pycharm project so if any of your file name is same name of module it will show that as its
#not a packages.so never make file name similar to module
import file2
print(file2.timepass("so just enjoy it"))
from time import time



a=time()
print(a)               #time module.
n=int(input())
if n==1:
    print("aur kaisan baa",time()-a)
print(time())
