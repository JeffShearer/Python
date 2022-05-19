# filter for a variable
for value in [1,20,341,2000,9] :
    if value > 100:
        print('big number', value)

# search for a variable
found = False
for value in [9,0,3,10,20,3]:
    if value == 3 :
        found = True
        break
    print(found,value)
print('after', found)