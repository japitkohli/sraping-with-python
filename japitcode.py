import bs4
import requests
import lxml
res=requests.get('https://en.wikipedia.org/wiki/Cricket')
soup=bs4.BeautifulSoup(res.text,'lxml')
soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text)
    
