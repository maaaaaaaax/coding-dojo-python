# compare_lists

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

list_a = list_one
list_b = list_four

if len(list_a) != len(list_b):
    print "The lists are not the same."
else:
    for index in range (len(list_a)):
        if list_a[index] != list_b[index]:
            print "The lists are not the same."
    print "The lists are the same."
