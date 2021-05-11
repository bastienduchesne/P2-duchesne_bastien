import requests
from bs4 import BeautifulSoup
import csv
for i in range(4):
  

url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
if r.ok:
  links = []
  h3 = soup.findAll('h3')
  for h in h3 :
    a = h.find('a')
    link = a['href']
    links.append('https://books.toscrape.com/catalogue'+ link)
    


"""
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

                    
with open('livre_info.csv','w', newline='') as file:
  fieldnames = ['product_page_url','universal_ product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating/5','image_url']
  writer = csv.DictWriter(file, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'product_page_url': url ,'universal_ product_code' : upc ,'title': title ,'price_including_tax' : price_incl_tax ,'price_excluding_tax' : price_excl_tax ,'number_available' : availability ,'product_description' :  description ,'category' : categorie ,'review_rating/5' : rating ,'image_url' : image})
 """
   


