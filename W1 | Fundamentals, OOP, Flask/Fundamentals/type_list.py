l = ["magical", "unicorns", 8, 5, "can", 13, "fly"]

# l = [1,2,3,4]

# l = ["hi", "my", "name", "is"]

# set i to current index of l, loop through until end

i = 0
mixed = 0
total = 0
string_total = []
list_type = []

if type(l[0]) == int:
    list_type = "integer"
    while i < len(l):
        if type(l[i]) == int:
            total = (total + l[i])
        if type(l[i]) != int:
            mixed = 1
        i = i + 1

if type(l[0]) == str:
    list_type = "string"
    while i < len(l):
        if type(l[i]) == str:
            string_total.append(l[i])
        if type(l[i]) != str:
            mixed = 1
        i+= 1

if mixed == 1:
    list_type = "mixed"
    i = 0

if (type(l[0]) != int) and (mixed == 1):
    while i < len(l):
        if type(l[i]) == int:
            total = (total + l[i])
        i+= 1

if (type(l[0]) != str) and (mixed == 1):
    while i < len(l):
        if type(l[i]) == str:
            string_total.append(l[i])
        if type(l[i]) != str:
            mixed = 1
        i+= 1

joined_string = ' '.join(string_total)

print "The list you entered is of " + list_type + " type"
if (type(l[0]) == str) or (mixed == 1):
    print "String: " + str(joined_string)
if (type(l[0]) == int) or (mixed == 1):
    print "Sum: {}".format(total)
