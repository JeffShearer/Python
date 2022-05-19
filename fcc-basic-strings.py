# index operatior - find a character within a string. starts at 0, much like JS. 
fruit = 'banana'
x = 3
w = fruit[x-1]
print (w)

#len function gives string length.
print('char length: ', len(fruit))

# or iterate through a string - indeterminate loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index, letter)
    index = index + 1

# or more elegantly with a determinate loop:
for letter in fruit:
    print(letter)
    

# or counting letters in a string:
fruit = 'banana'
count = 0 
for letter in fruit :
        if letter == 'a' :
            count = count + 1
print('"a" letter count:', count)