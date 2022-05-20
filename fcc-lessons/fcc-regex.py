# have to import the library before you can use it in python. w/ import re
# re.search(query,variable) which will give a true false, and re.findall() which will give you a list.

#match and extract example

import re
x = 'my 2 favorite numbers are 23 and 32'
# [0-9]+ is a regex that says find one or more digits.
y = re.findall('[0-9]+',x)
print(sorted(y,reverse=True))
