import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.passiton.com/inspirational-quotes"
r = requests.get(URL)

#print(r.content)     # this prints raw HTML content of the URL used

soup = BeautifulSoup(r.content, 'html5lib')     # passing raw HTML content to html5lib parser

# print(soup.prettify())                          # prints a clean HTML content, you can verify it by going to that URL and cmomparing with the "view page source" option

quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 

# print(table.prettify())                         # to check which piece of HTML we have filtered
   
for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)


filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)


