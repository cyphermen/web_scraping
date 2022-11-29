import requests
from bs4 import BeautifulSoup
import re

# change the URL
webpage = 'URL'
response = requests.get(webpage)
soup = BeautifulSoup(response.text, "html.parser")

# images
images = soup.find_all('img', attrs={'src': re.compile("^https://")})

# links
links = soup.find_all("a", href=True)

# print images one-by-one
print('images: ')
print('')
for image in images:
    print(image['src'])

# print links one-by-one
print('***************************************************************************************************************')
print('links:')
print('')
for link in links:
    print(link['href'])

# print images as a list
print('')
srcs = []
for image in images:
    srcs.append(image["src"])
print('images list: ', srcs)

# print links as a list
links_as_list = []
for link in links:
    links_as_list.append(link['href'])
print('links list:', links_as_list)
