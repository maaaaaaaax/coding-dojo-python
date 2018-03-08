# to open the python shell, type python in terminal. to exit, type exit(). to run a file, type python python_notes.py (example)

# printing strings using variables, a few methods:

# The first is by adding a comma after the string, followed by the variable.
# Note that the comma is outside the closing quotation mark of the string. Print inserts a space between elements separated by a comma.

name = "Max"
print "My name is", name


# The second is by concatenating the contents into a new string, with the help of +

name = "Max"
print "My name is " + name


# string interpolation:

first_name = "Max"
last_name = "Wiederholt"
print "My name is {} {}".format(first_name, last_name)


# Built-In String Methods
# String methods are functions that we can run on a string. Here's how to use these methods:

x = "Hello World"
print x.upper()
# output:
# "HELLO WORLD"

# The following is a list of commonly used string methods:
# string.count(substring): returns number of occurrences of substring in string.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

# full list available at https://docs.python.org/2.6/library/string.html


# In Python, arrays are called lists. Think of a list like a dresser with multiple drawers in which each drawer stores some information.

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

print my_list[1][1]
# output is 'in'

# Manipulating Lists
# Here's a useful example of a method that we will use to manipulate lists:
#
#<list>.append(<new_element>)
#
# Appends a new item onto the end of the given list. You can pass any data type into this function.

x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]

#It's important to know that Python uses [ ] characters to return a copy of the list, constrained to the specified indices. This can be thought of as behaving like the slice function in JavaScript. The starting index and ending index should be separated by the ":" character.

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];


# List Built-in Functions
# Below is an example of a built-in function that deals with lists. The following functions can also be applied to all sequences, including tuples and strings. What do we mean when we say sequence? Think of a sequence as anything over which we can iterate. Here's one commonly used sequence function:
#
# len(sequence): Returns the number of items in a sequence.

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output is 3

# Some built-in functions for sequences:
# enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence

# List Built-in Methods
# Below is an example of a built-in list method. These methods are specific to lists versus other sets, much like the string methods shown in the previous tab.
#
# list.append(value)

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
# output:
# [1,5,2,8,4,7]

# The following are some commonly used list methods:
# list.extend(list2) adds all values from a second sequence to the end of the original sequence.
# list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
# list.index(value) returns the index position in a list for the given parameter.

# See http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html for all list methods

# if statement:
# if condition:
  # do something
# if-else statement:
# elif condition:
  # do something
# else:
  # do this inst

age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'


# logic operators
# write out and and or

# (1 <= 2 and 2 <= 3)

# full docs here https://docs.python.org/2/library/stdtypes.html

# basic syntax for a for loop
# for <counter> in <sequence or range>:
  # do something

for count in range (0, 5):
    print "looping - ", count
# output is
# looping -  0
# looping -  1
# looping -  2
# looping -  3
# looping -  4

my_list = [4, 'dog', 99, ['list','inside','another'], 'hello, world!']
for element in my_list:
    print element

# rewriting our previous for loop as a while loop
count = 0
while count < 6:
    print 'looping - ', count
    count += 1

# The break statement exits the current loop prematurely, resuming execution at the first post-loop statement, just like the traditional break found in C or JavaScript.
# The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop. The break statement can be used in both while and for loop. When loops are nested, a break will only exit from the innermost loop.

for val in "string":
  if val == "i":
    break
  print val

# The continue statement returns the control to the beginning of the loop. The continue statement rejects -- or skips -- all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop. The continue statement is very useful when you want to skip one or more loop iterations, but keep looping to the end.

for val in "string":
  if val == "i":
    continue
  print val

# output:
# s
# t
# r
# n
# g


# x='1' and y = 2 turn an int to string: print x + str(y)


## FUNCTIONS

# functions notes. A function is a named block of code that we can execute to perform a specific task

def add(a,b):
  x = a + b
  return x

# the return value gets assigned to the "result" variable

result = add(3,5)
print result # this should print 8


# this function has one parameter(input)
def say_hi(name):
  print "Hi, " + name

# invoking the function passing in one argument
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')
# In this example 'name' is a parameter while "Michael", "Andrew", and "Jay", are arguments. We define parameters. We pass in arguments into functions.

# a functional call is equal to whatever that function returns.



## TUPLES

# Like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed. But we can add and slice tuples. See example below:

dog = ("Canis Familiaris", "dog", "carnivore", 12)

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

# You may recognize some of these built-in functions for sequences:
# max(sequence) returns the largest value in the sequence
# sum(sequence) return the sum of all values in sequence
# enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
# map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
# min(sequence) returns the lowest value in a sequence.
# sorted(sequence) returns a sorted sequence


## DICTIONARIES

# A Dictionary is another mutable set type that can store any number of Python objects, including other set types. Dictionaries consist of pairs (called items) of keys and their corresponding values.

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print weekend["Sun"]
# output is Sunday
print capitals["svk"]
# output is Bratislava

# Each key in a dictionary must be unique. If you make an assignment using an existing key as the index, the old value associated with that key is overwritten by the new value.

# Accessing Values

#to print all keys
for data in capitals:
     print data
#another way to print all keys
for key in capitals.iterkeys():
     print key
#to print the values
for val in capitals.itervalues():
     print val
#to print all keys and values
for key,data in capitals.iteritems():
     print key, " = ", data

# Python includes the following standalone functions for dictionaries:

# cmp(dict1, dict2) - Compares two dictionaries. The comparison process starts with the length of each dictionary, followed by key names, followed by values. The function returns 0 if the two dicts are equal, -1 if dict1 > dict2, 1 if dict1 < dict2.
# len() - give the total length of the dictionary.
# str() - produces a string representation of a dictionary.
# type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dictionary type.

# Methods
# .clear() - removes all elements from the dictionary
# .copy() - returns a shallow copy dictionary
# .fromkeys(sequence, [value] ) - create a new dictionary with keys from sequence and values set to value.
# .get(key, default=None) - For key key, returns value or default if key is not in dictionary.
# .has_key(key) - returns true if a given key is available in the dictionary, otherwise it returns false.
# .items() - returns a list of dictionary's (key, value) tuple pairs.
# .keys() - return a list of dictionary keys.
# .setdefault(key, default=None) - similar to get(), but will set dict[key]=default if key is not already in dictionary.
# .update(dict2) = adds dictionary dict2's key-values pairs to an existing dictionary.
# .values() - returns list of dictionary values.


# Nested Dictionaries

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

 # To iterate the values, we can use the nested for loop

for key, data in context.items():
    #print data
    for value in data:
        print "Question #", value["id"], ": ", value["content"]
        print "----"

# Question # 1 :  Why is there a light in the fridge and not in the freezer?
# ----
# Question # 2 :  Why don't sheep shrink when it rains?
# ----
# Question # 3 :  Why are they called apartments when they are all stuck together?
# ----
# Question # 4 :  Why do cars drive on the parkway and park on the driveway?
# ----

#
# Setting up
# If you haven't already installed virtualenv, do that now! Run this command:
# sudo pip install virtualenv

# $ cd ~/Documents/CodingDojo/python_stack/myEnvironments

# While in the parent directory to our virtual environments (myEnvironments), activate the virtual environment by typing:
# source flaskEnv/bin/activate

#  To deactivate your virtual environment, just type deactivate in the command line. Closing your terminal window will deactivate your virtual environment. If you do so, simply activate it again.
