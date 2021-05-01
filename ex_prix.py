import requests
from bs4 import BeautifulSoup



url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

r = requests.get(url)

if r.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    product_page_url = url

    """
    price_including_tax = soup.find('tr' , {'id': 'incl'}).find('td')
    price_excluding_tax = soup.fin('tr' , {'id': 'excl'}).find('td')
    number_available = soup.fin('tr' , {'id': 'Availability'}).find('td')
    """
    trs = soup.findAll('tr')
    title = soup.h1.text
    description = soup.findAll('p')
    rating = soup.find('p' , {'class': 'star-rating '})
    soup.article.children
  
  
    
    
    """
    for tr in trs:
        if tr.th.text == 'UPC':
          print(tr.td.text)
        if tr.th.text == 'Price (excl. tax)':
          print(tr.td.text)
        if tr.th.text == 'Price (incl. tax)':
          print(tr.td.text)
        if tr.th.text == 'Availability':
          print(tr.td.text)
"""


   
