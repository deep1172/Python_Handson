from plyer import notification  
import requests 
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title =title,
        message = message,
        app_icon = "C://Users//Administrator//OneDrive//Desktop//Butterscotch//Covid Notification//covid19.ico ",
        timeout= 10
    )
def getData(url):
    r= requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
    # notifyMe("Deep","Lets stop this covid-19 pandemic")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        # print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDatastr =""
        for tr in soup.find_all('t_body')[1].find_all('tr'):
            myDatastr += tr.get_text()
        myDatastr =myDatastr[1:]    
        itemList = myDatastr.split('\n\n')

        for item in itemList[0:22]:
            print(item.split('\n'))

        states = ['West Bengal', 'Bihar', 'Uttar Pradesh']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states: 
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)

