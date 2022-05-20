# XML example - parse a block of HTML - have to import the xml library first.

import xml.etree.cElementTree as ET
# note triple quotes will include additonal lines in the same item
data = '''<person>
<name>Jeff</name>
<phone type = "intl">
+1 425 111 111
</phone>
<email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))