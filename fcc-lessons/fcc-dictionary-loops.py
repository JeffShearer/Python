# count words in an external file name, find the most commmon word and read out the word, and the count
# this is the first real application built so far. lot to unpack so I've commented inline to remind myself how all this works.

handle = open('words.txt')

# initialize an empty dictionary
counts = dict()
# for each line in the text file, split the words into individual list items
for line in handle:
    words = line.split()
    # Then take those words, count their occurences, and put the word and their total counts into the dictionary you intialized earlier
    for word in words:
        counts[word] = counts.get(word,0) +1

# initialize two new variables for the highest frequency word, and it's cooresponding count
bigcount = None
bigword = None

#loop through the counts dictionary with BOTH word and count
for word,count in counts.items():
    # each time through the loop - if the word you're looking at has a higher count than the current bigcount, then make that the new bigcount
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Biggest word:', bigword, 'Count:', bigcount)