# adding a new line - note "\n" is a single character, not two.
#in a txt file, each line break ends with a \n. empty lines have a single character, a newline (\n)

stuff = 'Hello\nWorld'
print(stuff)

#opening a file, in this case, the readme.md in this folderm, and strips whitespace out.
fhand = open('sample.txt')
linecount = 0
for line in fhand :
    line=line.rstrip()
    linecount = linecount + 1
    print(line)
print('line count:', linecount)



#counting subject lines in a text file, and verifies the file exists to not spit an error.

fname = input('what\s the file name? ')
# try statement checks if the file will actually load, and if not, lets user know it's not a real file
try : 
    fhand = open(fname)
except : 
    print('No such file', fname)
    quit()
# then sets a counter and increments it for each line that starts with a subject line, and finally prints the result. 
count = 0
for line in fhand:
    if line.startswith('Subject') :
        count = count + 1
print (count, 'subject lines in', fname)


