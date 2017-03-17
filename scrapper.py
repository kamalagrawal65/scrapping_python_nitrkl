import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles")
#print r.content    #orignal file from source code

soup=BeautifulSoup(r.content,"html.parser")
print(soup.purify)
