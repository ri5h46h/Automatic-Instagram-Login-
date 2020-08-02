'''library requirements :
pip install beautifulsoup4
pip install requests
pip install pyttsx3
pip install plyer
pip install html5lib
sudo apt install python3-dbus (if using ubuntu/debian)'''


from bs4 import BeautifulSoup 
import requests
import pyttsx3
from plyer import notification

def getData(url):
    r = requests.get(url)
    return r.text

def speak(str):
    pass

def notifyfunc(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10,
    )



if __name__ == '__main__':
    htmlData = getData('https://distrowatch.com/dwres.php?resource=popularity')
    # print(htmlData)
    soup = BeautifulSoup(htmlData, 'html.parser')
    # print(soup)
    # for a in soup.find_all('table')[13].find_all('a'):
    topList = []
    for a in soup.find_all('table')[13].find_all('a'):
        topList.append(a.get_text())
        
print(topList[:6])
notifyTitle = "Top Linux Distros of last 1 month"
notifyMessage = str(topList[:6])

engine = pyttsx3.init()

notifyfunc(notifyTitle,notifyMessage)

engine.say(notifyMessage)
engine.runAndWait()


        
    
      
        

