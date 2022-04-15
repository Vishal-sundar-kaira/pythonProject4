#this is used to import some link or use it.
#it help to open and read any link .
import requests
r=requests.get("https://api.github.com/events")  #this will help us to excess that link information.
#print(r.text)
# pay={"vishal":"programmer","sahil":"manager"}
# r=requests.post("https://httpbin.org/post",params=pay) #params used to make changes and add string in url.
#print(r.url)
#this also used to share iformation on given link to verify it.
print(r.text)