import xml.etree.ElementTree as ET #import as a short form
data = ''' <person>
<name>Chuck</name> 
<phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide ="yes"/>
</person>
'''

tree = ET.fromstring(data) #parses the xml data into string
print('Name: ',tree.find('name').text) #Find the info on 'name' class
print('Attr: ',tree.find('email').get('hide'))#find the email class and get the status of it
