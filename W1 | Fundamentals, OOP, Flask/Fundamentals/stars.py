# Create a function called draw_stars() that takes a list of numbers and prints out *.
# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following when invoked:
# ****
# ******
# *
# ***
# *****
# *******
# *************************


# lst = [4, 6, 1, 3, 5, 7, 25]
#
# def draw_stars(lst):
#     # store the index value in a local variable
#     # create a new string for that row
#     length = len(lst)
#     index = 0
#     while length > 0:
#         number_of_stars = lst[index]
#         # print number_of_stars
#         string_for_this_row_so_far = ""
#         while number_of_stars > 0:
#             string_for_this_row_so_far = string_for_this_row_so_far + "*"
#             number_of_stars = number_of_stars - 1
#         print string_for_this_row_so_far
#         length = length - 1
#         index = index + 1
#
# draw_stars(lst)


lst = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(lst):
    # store the index value in a local variable
    # create a new string for that row
    length = len(lst)
    index = 0

    while length > 0:
        if type(lst[index]) == int:
            number_of_stars = lst[index]
        if type(lst[index]) == str:
            number_of_stars = len(lst[index])
            # print number_of_stars
            string_first_letter = ""
            string_first_letter = string_first_letter + str(lst[index][0])
        # print number_of_stars
        string_for_this_row_so_far = ""
        while number_of_stars > 0:
            if type(lst[index]) == int:
                string_for_this_row_so_far = string_for_this_row_so_far + "*"
            if type(lst[index]) == str:
                string_for_this_row_so_far = string_for_this_row_so_far + str(string_first_letter)
            number_of_stars = number_of_stars - 1
        print string_for_this_row_so_far.lower()
        length = length - 1
        index = index + 1

draw_stars(lst)
