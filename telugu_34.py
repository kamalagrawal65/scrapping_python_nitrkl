import urllib.request
from bs4 import BeautifulSoup

def downloadURL(url):

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    soup = BeautifulSoup(respData,'html.parser')
    paras = soup.find_all('font')
    name = url.split('?')
    # print(name)

    outputFile = open(name[1]+'.txt','w')
    for i in range(0,len(paras)):
        if i%3==0:
            outputFile.write(paras[i].text)


    outputFile.close()

    print('Copied to file : '+name[1]+'.txt')


if __name__ == "__main__":

    url = input("Enter the url of the article : ")    #'http://www.eenadu.net/homeinner.aspx?category=home&item=break139'
    downloadURL(url)
