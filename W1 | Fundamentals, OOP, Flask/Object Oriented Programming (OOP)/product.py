# product.py

# declare a class and give it name User
class Product(object):
    # the __init__ method is called every time a new object is created
    # Price and Weight are integers; item_name, brand, and status are strings
    def __init__(self, price, item_name, weight, brand):
        # set some instance variables. just like any variable we can call these anything
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    # this is a method we created to help a user login
    def sell(self):
        self.status = "sold"
        return self
    # takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def addTax(tax):
        self.price_plus_tax = self.price + (self.price * tax)
        print "Price after tax is {}".format(self.price_plus_tax)
        return self.price_plus_tax
    # takes strings as arguments: "defective", "like_new", "used"
    # Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
    def refund(condition):
        if condition is "defective":
            self.status = "defective"
            self.price = 0
        if condition is "like_new":
            self.status = "for sale"
        if condition is "used":
            self.status = "used"
            self.price = (self.price * 0.5)
        return self
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Item Name: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return self

#now create an instance of the class
product1 = Product(800,"iPhone8",1,"Apple")

print product1.display_all()
