import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url= input('Enter url: ')
xml = urllib.request.urlopen(url).read()
print("Retrieving:",url)

tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
print('Count:',len(lst))

sum = 0
for item in lst:
    number = item.find('count').text
    num = int(number)
    sum+= num

print('Sum:',sum)




