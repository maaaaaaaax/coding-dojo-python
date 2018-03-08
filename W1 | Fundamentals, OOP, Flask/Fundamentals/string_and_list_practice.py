words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
# output is the index for the first character in the string: 18
new_words = words.replace("day", "month", 1)
print new_words
#output is It's thanksgiving month. It's my birthday,too!


x = [2,54,-2,7,12,98]
print min(x)
# output is -2
print max(x)
# output is 98

x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
last = x[(len(x)-1)]
print first
# output is hello
print last
# output is last
new_list = []
new_list.append(first)
new_list.append(last)
print new_list
# output is ['hello', 'world']







x = [19,2,54,-2,7,12,98,32,10,-3,6]
y = sorted(x)
print y
# output is [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]

# set z to the midpoint (round down if list is odd)
i = ((len(x) / 2))
j = (len(x) - i)
print i
print j
y_zero_index = []

for elements in range(i):
    y_zero_index.append(y[elements])

print y_zero_index
# output is [-3, -2, 2, 6, 7]

print y[(i):(len(x)-1)]
# output is [10, 12, 19, 32, 54]

new_list = y[(i):(len(x)-1)]

print new_list
new_list.insert(0,y_zero_index)
print new_list
