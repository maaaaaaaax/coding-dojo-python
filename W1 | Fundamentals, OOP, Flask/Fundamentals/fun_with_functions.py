def odd_even():
    for num in range(1,2001):
        if num % 2 == 0:
            print "Number is {}. This is an even number.".format(num)
        if num % 2 == 1:
            print "Number is {}. This is an odd number.".format(num)

# odd_even()


lst = [60,2,3]
list_one = [1,2,3,4]


def multiply(lst, factor):
    for num in range(0,len(lst)):
        lst[num] = lst[num] * factor
    print lst


multiply([1,2,3], 4)
