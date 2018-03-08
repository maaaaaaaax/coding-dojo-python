# Multiples, Sum, Average

# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for val in range (1, 1000):
    if (val % 2 == 1):
        print val

for val in range (5, 1000000):
    if (val % 5 == 0):
        print val



a = [1, 2, 5, 10, 255, 3]

sumOfA = 0

for val in range(len(a)):
    sumOfA = (sumOfA + a[val])

print sumOfA



a = [1, 2, 5, 10, 255, 3]

sumOfA = 0
avg = 0

for val in range(len(a)):
    sumOfA = (sumOfA + a[val])
    avg = (sumOfA / len(a))

print avg
