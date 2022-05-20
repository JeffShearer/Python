# dictionaries - a bag of values, each a key-value pair, vs a list which is all about position. 
# basically allow database-like operations in python, everything is indexed with a lookup tag.
#Dictionaries are unordered, unlike lists. 

opps = dict()
opps['ABC co'] = 3
opps['xyz co'] = 2
opps['acme corp'] = 1

print(opps)
print(opps['acme corp'])

# increment values to an existing dictionary entry
opps['acme corp'] = opps['acme corp'] + 1
print(opps)

# Building a histogram of frequency with a dictionary
counts = dict()
opps = ['abc co','abc co','xyz co','acme co','acme co','nobody co']
for company in opps :
    if company not in counts:
        counts[company] = 1
    else : 
        counts[company] = counts[company] + 1
print(counts)

# or use get method to simplify checking presence of value in the dictionary
counts = dict()
opps = ['abc co','abc co','xyz co','acme co','acme co','nobody co']
for company in opps :
    counts[company] = counts.get(company,0) + 1
print(counts)