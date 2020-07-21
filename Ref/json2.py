import json
data = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Granoba"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Mellucium"
    }
]'''

info = json.loads(data)
print('User count:', len(info)) #sees the lists length
for item in info:
    print('Name', item['name']) #searches name info 
    print('ID', item['id']) #searches id info
    print('Attribute', item['x']) #searches the association value to x

