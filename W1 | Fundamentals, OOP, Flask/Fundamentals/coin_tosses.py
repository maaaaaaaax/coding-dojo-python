# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

# Use the python built-in round function to convert that floating point number into an integer

# x = .23945593
# y = .798839238
# x_rounded = round(x)
# x_rounded will be rounded down to 0
# y_rounded = round(y)
# y_rounded will be rounded up to 1

# function returns either one or zero

import random

# function returns either one or zero
def toss():
    x = random.randint(0,1)
    heads_or_tails = round(x)
    return int(heads_or_tails)

print "Starting the program..."

# create a counter variable for how many tosses we have completed so far
counter = 0
# create a counter variable for number of 1's returned so far
heads = 0
# create a counter variable for number of 0's returned so far
tails = 0

for counter in range(1,5001):
    flip = toss()
    if flip == 0:
        tails = tails + 1
        print "Attempt #{}: Throwing a coin... It's heads! ... Got {} head(s) so far and {} tail(s) so far".format(counter, heads, tails)
    if flip == 1:
        heads = heads + 1
        print "Attempt #{}: Throwing a coin... It's tails! ... Got {} head(s) so far and {} tail(s) so far".format(counter, heads, tails)

print "Ending the program. Thank you!"
