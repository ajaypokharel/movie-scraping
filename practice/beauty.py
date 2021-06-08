import requests
from bs4 import BeautifulSoup as bs


r = requests.get("https://www.programiz.com/    ")

soup = bs(r.text, features="lxml")

needed = soup.find('footer', class_='footer')

matched = needed.div

print(matched.prettify())
