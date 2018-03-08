# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

# declare a class and give it name Car
class Car(object):
    # the __init__ method is called every time a new object is created
    # price is an integer, Speed a string ending in "mph", Fuel a string with options of "Full", "Not Full", "Kind of Full", or "Empty", Mileage is a string ending in mpg, and tax is a float of either 0.12 or 0.15
    def __init__(self, price, speed, fuel, mileage):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

# this is a method we created to help a user login
# display the car's attributes.
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self

#now create an instance of the class
car1 = Car(11000,"220mph","Full","22mpg")
car2 = Car(11000,"220mph","Full","22mpg")
car3 = Car(11000,"220mph","Full","22mpg")
car4 = Car(11000,"220mph","Full","22mpg")
car5 = Car(11000,"220mph","Full","22mpg")
