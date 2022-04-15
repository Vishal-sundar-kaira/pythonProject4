#akhbaar padke sunao excersice.
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.speak(str)
speak("hello welcome to vishal land")

if __name__ == '__main__':
    url="https://newsapi.org/v2/everything?q=tesla&from=2021-11-11&sortBy=publishedAt&apiKey=75c7fbc663db4439b83cdadb0ddf531c"
    a=requests.get(url).text
    news=json.loads(a)
    news_dict=news['articles']
    for i in news_dict:
     speak(i['title'])