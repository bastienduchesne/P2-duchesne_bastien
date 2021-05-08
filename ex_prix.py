import requests
from bs4 import BeautifulSoup
import csv


with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

r = requests.get(url)

if r.ok:
  soup = BeautifulSoup(r.text, "html.parser")
  product_page_url = url
  trs = soup.findAll('tr')
  title = soup.h1.text
 
  bread =  soup.find("ul", { "class" : "breadcrumb" }).find('li')
  categorie = bread.next_sibling.next_sibling.next_sibling.next_sibling.text
  description = soup.find("article", { "class" : "product_page" }).find("p", recursive=False).text
  image = soup.img['src']
  star = soup.find('p', class_="star-rating")
  rating = star.get('class')[1] 
    
  for tr in trs:
    if tr.th.text == 'UPC':
      upc = tr.td.text
    if tr.th.text == 'Price (excl. tax)':
      price_excl_tax = tr.td.text
    if tr.th.text == 'Price (incl. tax)':
      price_incl_tax = tr.td.text
    if tr.th.text == 'Availability':
      availability = tr.td.text

"""
with open('livre_info.csv','w', newline='') as outf:
  fieldnames = ['product_page_url','universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating/5','image_url']
  writer = csv.DictWriter(outf, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'product_page_url': url})
     #writer.writerow({'product_page_url':url,'universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating/5','image_url'
   # writer.writerow(url + ',' + upc + ',' + title + ',' + price_incl_tax + ',' + price_excl_tax + ',' + availability + ',' + description + ',' + categorie + ',' + rating + ',' + image + '/n')
   """


