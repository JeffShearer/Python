#basically the shortcut to the socket approach in fcc-networking-sockets.py
# uses a built in python library, urrlib

import urllib.request
#note - this method won't give you the file headers - just the content.
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# and then do whatever you want with it, like count iterations of a word in the file
#note you haver to make the request each time it seems.
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

# or retrieve web pages!

import urllib.request
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())