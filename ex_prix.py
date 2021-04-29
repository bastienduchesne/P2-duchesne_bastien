import requests
from bs4 import BeautifulSoup

url='https://books.toscrape.com/index.html'
r = requests.get(url)

if r.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    genre = soup.findAll('href')
print(len(genre))
