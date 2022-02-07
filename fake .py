from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html")
res = BeautifulSoup(html.read(),"html5lib")
print(res.title)
print(res.prettify)
print(res.find_all("h2"))
