from json import loads

data = '''
{
"name" : "chunk",
"phone" : {
"type" : "intl",
"number" : "9000017580"
},
"email" : {
"hide" : "yes"
}
}'''

info = loads(data)
print(info["name"])
print(info["phone"]["type"])
print(info["phone"]["number"])
print(info["email"]["hide"])