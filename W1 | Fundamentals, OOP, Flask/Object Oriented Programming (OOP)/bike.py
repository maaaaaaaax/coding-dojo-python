# declare a class and give it name User
class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # this is a method we created to help a user login
    # display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "The price of this bike is ${}, the maximum speed of this bike is {} mph, and this bike's mileage is {}.".format(self.price,self.max_speed,self.miles)
        return self
    def ride(self):
        self.miles = self.miles + 10
        print "Riding"
        return self
    def reverse(self):
        self.miles = self.miles - 5
        print "Reversing"
        return self

#now create an instance of the class
bike1 = Bike(1000,200)
print bike1.price
print bike1.displayInfo()
