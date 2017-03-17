from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get("http://" +url)
data = r.text

soup = BeautifulSoup(data)
#print(soup.prettify())         ##prints the source code in a beautiful form

#for link in soup.find_all('a'):
#    print(link)

#for link in soup.find_all('a'):
    #print(link.get('href'))
    #print(link.text)


gdata=soup.find_all("font")
#gdata=soup.find_all("div",{"class":"info"})
#print(gdata)

for item in gdata:
    print(item.text)
