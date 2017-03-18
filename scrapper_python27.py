from bs4 import BeautifulSoup
import requests
url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get(url)
data = r.text

soup = BeautifulSoup(data)
#print(soup.prettify())         ##prints the source code in a beautiful form

#for link in soup.find_all('a'):
#    print(link)

#for link in soup.find_all('a'):
    #print(link.get('href'))
    #print(link.text)


gdata=soup.find_all("p")
#gdata=soup.find_all("div",{"class":"info"})
#print(gdata)

fo=open("E:/ML/test/Dataset/e.txt",'a')

data=[]
for item in gdata: 
    data.append(item.text)

for i in range(0,len(data)):
    fo.write(data[i].encode('utf-8')+"\n")

print("Written to file.")
