# slicing - pulling chunks of a string
# [0:4] means up to, but not including 4.

from re import S


term = "Jeff S"
print (term[0:2])

# or omit one of the values to start at the beginning/ go to the end regardless of the string length
print(term[0:])


# use in to check if a string is "in" another:
term = "team"
if 'i' not in term : 
    print('there is no "i" in team')

# string libraries - methods are built in to python for string manipulation purposes
# These methods don't modify the original string - but create a new one.

# More at https://docs.python.org/3/library/string.html

greet = "HIYA"
new = greet.lower()
print(new)

#this will find the position of the character in the string.
i = greet.find("YA")
print(i)

#search and replace
greet = 'Hello Bob'
newgreet = greet.replace('Bob','Jane')
print(newgreet)
print(greet) #note - original string didn't change. 


#whitespace stripping

greet = '   hiya'
greet = greet.lstrip()
print(greet)


#parse and extract an email address example - seems particularly useful for marketing use cases.

data = 'from me@emailaddress.com Sat Jan 5 09:15:16 2022'
dotcom_pos = data.find('.com')
print(data[dotcom_pos:dotcom_pos+3])
sppos = data.find(' ', dotcom_pos)
print(sppos)
email = data[:sppos]
print(email)