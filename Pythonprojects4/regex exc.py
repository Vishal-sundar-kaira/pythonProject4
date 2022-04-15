#Email extractor.
#In this we need to take one string(large) in which there will be many emails and we just need to collect emails from them and store in file.
import re
string="""hello my name is vishal kaira my email id is kairavishal37@gmail.com, and my friend name is sahil whose email id is" \
       "sahilnegi@gmail.com, bittu whose email id is bittuyash@gmail.com, abhishek whose email id is absekpatil@gmail.com," \
       "welcome to our college whose email id is tsec@gmail.com."""
find=re.findall(r'sahil',string)   #be good in writing this \w means any alphabet (+) means 1 or more than 1 times.
match=str(find)
for match in find:
       print(match)
file=open("emails","a")
adding=file.write(match)
print(adding)
