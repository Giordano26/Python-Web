import urllib.request, urllib.parse, urllib.error
import json

url= input('Enter url: ')
inf = urllib.request.urlopen(url).read()
print("Retrieving:",url)

data = json.loads(inf)
print('Retrieved', len(inf),'characters')

soma = 0
comments = data['comments']
for comment in comments:
    number = comment['count']
    soma += number

print('Sum:',soma)