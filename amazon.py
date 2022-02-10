from urllib.request import urlopen
from bs4 import BeautifulSoup
html =urlopen("https://www.amazon.in/All-Mobile-Phones/s?k=All+Mobile+Phones")
soup = BeautifulSoup(html.read(), "html5lib")
print(soup.prettify)
mobile_price =soup.find(class_="a-price").span.text
mobile_feature = soup.find(id="title_feature_div")
print(mobile_price,mobile_feature)
