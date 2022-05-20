number = input('Enter a number:')
try:
    ival = int(number)
except:
        ival = -1

if ival > 0 :
    print('Your  number is ' + number)
else:
    print('you didnt\' enter a number')
