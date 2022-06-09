from xml.etree import ElementTree
input='''<stuff>
<users>
    <user x="2">
        <id>001</id>
        <name>Chuck</name>
    </user>
    <user x="7">
        <id>009</id>
        <name>Brunt</name>
    </user>
</users>
</stuff>'''

stuff = ElementTree.fromstring(input)
lst = stuff.findall('users/user')
for node in lst:
    print(node.find('name').text)
    print(node.find('id').text)
    print(node.get('x'))

