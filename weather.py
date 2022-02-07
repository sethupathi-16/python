import requests
from bs4 import BeautifulSoup
search = "weather in madhurai"
html =(f"https://www.google.com/search?q={search}")
r = requests.get(html)
s = BeautifulSoup(r.text,"html5lib")
update = s.find("div",class_="BNeawe").text
print(update)
