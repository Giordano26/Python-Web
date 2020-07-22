import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)#parses data from json
print('Name:', info["name"])#gets the json info from name
print('Hide:',info["email"]["hide"])#gets the json detail from email 