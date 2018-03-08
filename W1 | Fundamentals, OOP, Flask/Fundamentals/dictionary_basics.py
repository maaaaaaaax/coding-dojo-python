# dictionary_basics.py

user = {} #create an empty dictionary then add values
user["userIntegerID"] = 0000000000
user["first name"] = "Max"
user["last name"] = "Wiederholt"
user["username"] = "@maxwiederholt"
user["country of birth"] = "USA! USA! USA!"
user["state of birth"] = "California"
user["age"] = 25


# print user["state of birth"]
# output is @maxwiederholt

users = {"0000000000": {"userIntegerID": 0000000000, "firstName": "Max", "lastName": "Wiederholt", "username": "maxwiederholt"}, "0000000001": {"userIntegerID": 0000000001, "firstName": "Ben", "lastName": "Wiederholt"}}

# print users
# output is {'0000000000': {'username': 'maxwiederholt', 'lastName': 'Wiederholt', 'firstName': 'Max', 'userIntegerID': 0}, '0000000001': {'lastName': 'Wiederholt', 'firstName': 'Ben', 'userIntegerID': 1}}

# print users["0000000000"]["firstName"]

users["0000000000"]["birthdayDay"] = 8
# print users["0000000000"]["birthdayDay"]
# output is 8


dictionary = {"name": "Anna", "age": 101, "country of birth": "The United States", "favorite language": "Python"}

def print_dictionary(dictionary):
    for key in dictionary:
        print "My {} is {}".format(key,dictionary[key])

print_dictionary(dictionary)




# Question: can you nest a dictionary inside another dicitonary?

# You can declare a dictionary inside a dictionary by nesting the {} containers:
#
# d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}
# And then you can access the elements using the [] syntax:
#
# print d['dict1']           # {'foo': 1, 'bar': 2}
# print d['dict1']['foo']    # 1
# print d['dict2']['quux']   # 4
# Given the above, if you want to add another dictionary to the dictionary, it can be done like so:
#
# d['dict3'] = {'spam': 5, 'ham': 6}
