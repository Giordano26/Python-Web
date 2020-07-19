import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

count = input('Enter count: ')
count = int(count)

position = input('Enter position: ')
position = int(position)

names = []
i = 0
while(count > 0):
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    name = tags[position-1].string
    names.append(name)
    url = tags[position-1]['href']
    count-= 1

print(names)
    
    
