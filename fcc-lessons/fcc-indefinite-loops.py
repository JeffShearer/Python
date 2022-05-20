# while statemens are like if, but will continue to run over and over until they no longer qualify. (loops)
n = 0
while n < 10 :
    print(n)
    n = n + 2
print('blastoff!')
print(n)

# Breaks - lets you exit a loop entirely - below, basically if "done" is input, then the loop ends.

while True: 
    line = input('>')
    if line == 'done' : 
        break
    print (line)
print('done')

# Continue - lets you exit current iteration an jump to the next iteration

while True:
    line = input('>')
    if line[0] == 'nope' :
        continue #this sends the loop back to the top
    if line == 'done' :
        break #this ends the loop entirely
    print(line)
print('Done')