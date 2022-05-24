# collections - basically arrays, you can have many values in them.

friends = ['leia','luna']
for friend in friends : #note - python doesn't understand plural and singular.
    print('Hi', friend)

# changing elements of a list

numbers = [1, 20, 30]
numbers[2] = 5
print(numbers)
# len says # of items in a list. 
print('numbers in the list:', len(numbers))



# You can also concatenate lists

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# and slice them, just like strings. 
d = c[1:5]
print(d)
# You can also do some built in functions like sum
print('list total:', sum(c))

#Build a new list. first create an empty one
mylist = list()
mylist.append('book')
print(mylist) 


#split function - breaks string into parts and makes a list out of it. 
#note - split treats successive spaces as one.

abc = 'with    three words'
stuff = abc.split()
print(stuff)
# or split with an argument looking for some other deliminter (seems like exactly what you'd want to parse a CSV)
string = 'with-three-words'
stuff2 = string.split('-')
print(stuff2)

#or retrieve a specific element from a list - in this case, just return the YYYY-MM-DD from my list
fhand = open('sample.txt')
for line in fhand :
    line = line.rstrip()
    # below is a litte confusing - basically this says - if the line DOESN'T start with Date, repeat the next iteration until it does. 
    if not line.startswith('Date') :
            continue
    # this splits the date lines into a two item list
    words = line.split()
    # and this just prints the second item of that list (the actual date)
    print (words[1])

# or even more complex - just get the month of the date!

fhand = open('fcc-lessons\sample.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('Date') :
            continue
    words = line.split()
    date = (words[1])
    datenums = date.split('-')
    month = datenums[1]
    print(month)