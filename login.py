from selenium import webdriver as wb
import requests
from bs4 import BeautifulSoup as bs


URL = "https://torrentwal.net/torrent_variety/torrent1.htm"
response = requests.get(URL)

print(response.status_code)
htmlContent = response.content

text = bs(htmlContent, 'html.parser')

print(text.prettify())


#browser = wb.Edge()
#browser.get("https://torrentwal.net/torrent_variety/torrent1.htm")
#var = browser.
#print(var)


