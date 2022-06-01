

int_list = [[1,2],[3,4],[5,6],[7,8]]
string_list = ["a","b","c"]
subliststring = ""
listsum = 0

#Turning a list into a string is straightforward with += operator
for sublist in string_list:
    subliststring += str(sublist)

print(subliststring)

#Nested for loops look at the first set of values, with another loop below to go a level deeper to sum the elements of the list
for sublist in int_list:
    for number in sublist:
        listsum += number

print(listsum)