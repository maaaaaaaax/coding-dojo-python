# Strings
# https://docs.python.org/2.6/library/string.html#string.find
# capitalize
# upper
# lower
# count
# find
# index
# split
# join
# replace
# format

string_a = "hello"
y = string_a.capitalize()
print y
# output is Hello

string_b = "this is all lowercase"
c = string_b.upper()
print c
# output is THIS IS ALL LOWERCASE

print string_b.lower()
# output is this is all lowercase

print string_b.count('this')
# output is 1

words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
# output is 18

print words.find("dog")
# output is -1
# error, sort of

print words.index("day")
# output is 18

# print words.index("dog")
# output is ValueError: substring not found
# also, breaks any further code written past this error

print words.replace("day", "month", 1)

print words.split()
# output ["It's", 'thanksgiving', 'day.', "It's", 'my', 'birthday,', 'too!']

first_name = "Max"
last_name = "Wiederholt"

split_string = ["Coding","Dojo","is","located","in","San","Jose"]
print split_string
# output is ['Coding', 'Dojo', 'is', 'located', 'in', 'San', 'Jose']
joined_string = ' '.join(split_string)
print joined_string
# output is Coding Dojo is located in San Jose

sum = 0
for x in range(10):
    if x % 2 == 0:
        sum += x

print("Sum: {}".format(sum))
#Sum: 20

x = [1,2,3]
print len(x)
# output is 3
print max(x)
# output is 3
print min(x)
# output is 1

print x.index(2)
# output is 1

x.append(5)
# doesn't return anything
print x
# output is [1, 2, 3, 5]
print x.pop()
# output is 5

zach = [1,2,3]
print x.pop(1)
# output is 2
print x
# output is [1, 3]

decimal = [0,1,2,3,4,5,6,7,8,9]
print decimal.remove(8)
# output is None
print decimal
# output is [0, 1, 2, 3, 4, 5, 6, 7, 9]

decimal = [0,1,2,3,4,5,6,7,8,9]
print decimal.insert(1,12)
# output is none
print decimal
# output is [0, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]

drunk_decimal = [0,9,1,8,2,7,3,6,4,5]
print drunk_decimal
print drunk_decimal.sort()
# output is none
print drunk_decimal
# output [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

decimal = [0,1,2,3,4,5,6,7,8,9]
print decimal
print decimal.reverse()
print decimal

xxx = ["bananas", "eggplants", "cucumbers", "zucchini"]
print xxx
xxxx = ["pineapples", "peaches", "grapes"]
print xxx.extend(xxxx)
print xxx
# ['bananas', 'eggplants', 'cucumbers', 'zucchini', 'pineapples', 'peaches', 'grapes']

zach_is_my_favorite_tuple = ("Zach", 0, "OOhhh", 1)
print zach_is_my_favorite_tuple
print list(zach_is_my_favorite_tuple)
# ['Zach', 0, 'OOhhh', 1]




# Lists
# https://www.tutorialspoint.com/python/python_lists.htm
# len
# max
# min
# index
# append
# pop
# remove
# insert
# sort
# reverse
# (optional) extend
# (optional) list
