# basic counting in a loop
i = 0
for y in [1,2,3,4,5,6,10,21] :
    i = i + 1
    print ('count:', i, 'value:', y)
print('after, i')

# summing & averaging a loop - sum is used as a running total, count is used for the final denominator for the avreage calculation
sum = 0
count = 0
for value in [9,10,2141,215,3021] :
    sum = sum + value
    count = count + 1
    print('running total:', sum)
    print('running count:', count)
print('grand total:', sum)
print ('average:', sum / count)
