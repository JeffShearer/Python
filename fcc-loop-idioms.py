# this finds the smallest nubmer in a list and keeps it to output at the end. 
# note - "None" is actually a constant - special property in python. 
#also note "is" is stronger than ==. Basically === in JS. Don't overuse it with numbers. good with booleans, none types.

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 2, 74, 15]:
    if smallest == None or itervar < smallest:
        smallest = itervar
    print("smallest so far: ", smallest)
print("Smallest:", smallest)