import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
 
url = input('Enter url:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
soma = 0
count = 0
tags = soup('span')

for tag in tags:
    nums = int(tag.contents[0])
    soma += nums
    count += 1
print(soma)
print(count)