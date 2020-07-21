import xml.etree.ElementTree as ET
input = '''<stuff>
        <users>
            <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x ="7">
            <id>009</id>
            <name>Brent</name>
        </user>
        </users>
    </stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #lists and findall gets all the user below info
print('User count', len(lst))
for item in lst: #iterate trough the list and get name id and attribute
    print('Name', item.find('name').text) 
    print('ID',item.find('id').text)
    print('Attribute', item.get("x"))
