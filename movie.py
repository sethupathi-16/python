from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(html.read(),"html5lib")
print(soup)
movies=soup.find('tbody', class_="lister-list").find_all("tr")
for movie in movies:
   #print(movie)
   # movie_rang = movie.find('td', class_="titlecolumn").get.text
    movie_name = movie.find('td', class_="titleColumn").a.text
    movie_rate = movie.find('td', class_="ratingColumn").strong.text
    movie_year = movie.find('td', class_="titleColumn").span.text
    print(movie_name,movie_rate,movie_year)

  
  

