# Tuples use parentheses, not brackets. but unlike lists, you can't change them for efficiency's sake. 
# If all you want to do is create a list and look at it, a tuple is the way to go. 

# you can put a tuple on the left side of teh assignment, and it will assign properly, e.g.
(x,y) = (4,'fred')
print(y)

# Note these are also used when you pass multiple variables into a for statement - that's actually passign a tuple 
# (see fcc-dictionary-loops.py)

# sorted function - will sort in ascending, but you can put in arguments to revrse, aka
tmp= (1,2,3)
tmp = sorted(tmp,reverse=True)
print(tmp)


# Finding the top 10 most common words example The first paragraph is just what we've done in the past
#create a dictionary, split the lines and words into separate elements, add the count of the words as the value in the dictionary.
fhand = open('words.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Now we're creating an empty list, and inserting the key,value pairs in the dictionnry 
lst = list()
for key, val in counts.items():
    # Note - the order of key,val is swapped here, so the first item in the tuple is the value.
    newtup = (val,key)
    lst.append(newtup)

#then we can simply sort the list in reverse order
lst = sorted(lst,reverse=True)

# and then retrieve the top 10 items in that list via [:10]
for val,key in lst[:10]:
    print(key,val)

