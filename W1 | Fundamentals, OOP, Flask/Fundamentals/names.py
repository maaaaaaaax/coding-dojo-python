# names.py

students = [
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# print students[0]['first_name']

# for key in range(len(students)):
#     print "{} {}".format(students[key]['first_name'],students[key]['last_name'])



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# index = 0
# student_number = 1
#
# print users['Students'][index]['first_name']
# # output is Michael
#
# print users['Students'][index]['last_name']
# # output is Jordan
#
# student_name_length = len(users['Students'][index]['first_name']) + len(users['Students'][index]['last_name'])
# print student_name_length
# # output is 13
#
# this_row = "{} - {} {} - {}".format(student_number,users['Students'][index]['first_name'],users['Students'][index]['last_name'],student_name_length)
# print this_row.upper()
# # output is 1 - MICHAEL JORDAN - 13
#
# print len(users['Students'])
# # output is 4



def printStudentsRows():
    index = 0
    student_number = 1
    while index < len(users['Students']):
        student_name_length = len(users['Students'][index]['first_name']) + len(users['Students'][index]['last_name'])
        this_row = "{} - {} {} - {}".format(student_number,users['Students'][index]['first_name'],users['Students'][index]['last_name'],student_name_length)
        print this_row.upper()
        student_number = student_number + 1
        index = index + 1


def printInstructorsRows():
    index = 0
    instructor_number = 1
    while index < len(users['Instructors']):
        instructor_name_length = len(users['Instructors'][index]['first_name']) + len(users['Instructors'][index]['last_name'])
        this_row = "{} - {} {} - {}".format(instructor_number,users['Instructors'][index]['first_name'],users['Instructors'][index]['last_name'],instructor_name_length)
        print this_row.upper()
        instructor_number = instructor_number + 1
        index = index + 1


def names():
    print "Students"
    printStudentsRows()
    print "Instructors"
    printInstructorsRows()

names()
