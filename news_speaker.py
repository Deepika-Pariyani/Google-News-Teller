from GoogleNews import GoogleNews
import pyttsx3 as pt
news = GoogleNews()
news = GoogleNews(period='7d')
news.search('INDIA')
result = news.result()
for x in result:
    print("-"*50)
    speak =pt.init()
    title = x['title']
    date = x['date']
    desc = x['desc']
    speak.say("Title")
    speak.say(title)
    print("Title--",x['title'])
    speak.say("Date/Time")
    speak.say(date)
    print("Date/Time--",x['date'])
    speak.say("Description")
    speak.say(desc)
    print("Description--",x['desc'])
    print('link--',x['link'])
    speak.runAndWait()


