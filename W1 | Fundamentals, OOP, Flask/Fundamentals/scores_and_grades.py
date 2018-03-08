# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score.

import random

def print_line():
    import random
    # generate a random integer between 60 and 100, inclusive
    percent = random.randint(60,100)
    # while percent > 60:
    #     percent = random.random() * 100
    if percent < 70 and percent >= 60:
        letter = "D"
    if percent < 80 and percent >= 70:
        letter = "C"
    if percent < 90 and percent >= 80:
        letter = "B"
    if percent <= 100 and percent >= 90:
        letter = "A"
    return "Score: {}; Your grade is {}".format(percent, letter)

print "Scores and Grades"
for i in range(0,10):
    print print_line()
print "End of the program. Bye!"
