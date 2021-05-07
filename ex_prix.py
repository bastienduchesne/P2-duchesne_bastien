import requests
from bs4 import BeautifulSoup
import csv



url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

r = requests.get(url)

with open('livre_info.csv','w') as outf:
  outf.write('product_page_url,universal_ product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category,review_rating/5,image_url/n')
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
      outf.write(url + ',' + upc + ',' + title + ',' + price_incl_tax + ',' + price_excl_tax + ',' + availability + ',' + description + ',' + categorie + ',' + rating + ',' image +'\n')
          


   
