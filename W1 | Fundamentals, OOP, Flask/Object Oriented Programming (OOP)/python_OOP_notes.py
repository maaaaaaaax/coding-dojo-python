# python object oriented programming (OOP) notes

# Object oriented programming. Think of buildings in Age of Empires.
#
# A building has classes
#
# Attributes are variables inside a class
# Methods are functions inside a class
#
# Objects are also called instances
#
# Each instance will have its own x and y coordinate, health, and methods.
# Instance attributes or instance methods are unique to that instance
#
# A .constructor is a method that runs when a new instance is created
#
# Inheriting - say you upgrade a building in Age of Empires.
# You want your new barrack class two to inherit all the classes and methods from your original object.

# This is the finalized code of the class User that we are going to write incrementally throughout the following tabs:

# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = True
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self

#now create an instance of the class
id1 = User("Anna","anna@anna.com")
id0 = User("Max","max.wiederholt@gmail.com")
print id0000000000.email

# You can easily create a class in Python by typing the keyword class followed by the name of your class and (object).
class User(object):
    pass

# You should notice that we define one parameter object. When the parameter for a class is object it simply means that this class inherits from the object class. We'll get into inheritance a little more later on. You'll notice the keyword pass in the body - it is used as a placeholder where some code is required. It means do nothing.

# Think of the class as a blueprint for creating something. Once we've finished our blueprint we can create instances of this class. The User class we defined above is a blueprint for creating users. We create a new instance by using the class name as if it were a function. Let's go ahead and make instances of our User class

michael = User()
anna = User()

# print michael, anna

#Classes / objects include two types of things:
#
# Attributes: Characteristics shared by all instances of the class type. Take our User class, for example. All users have a name and an email. You might be wondering how each user can have a different name and email. We'll show you in the following tab.
# Methods: Actions that an object can perform. A user, for example, might be able to make a purchase. A method is like a function that belongs to a class. It's some instructions that will only work when called on an object that has been created from that class. We'll show you how shortly.

# A class: Instructions on how to build many objects that share characteristics.
# An object: A data type built according to specifications provided by the class definition.
# An attribute: A value. Think of an attribute as a variable that is stored within an object.
# A method: A set of instructions. Methods are functions that are associated with an object. Any function included in the parent class definition can be called by an object of that class.


# INHERITANCE
# Inheritance is forming new classes using classes that have already been defined. The benefits of inheritance are code reuse and reduction of complexity of a program.

class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self

# Implicit Inheritance
# Now we want to create new (sub)classes that are able to use all of the function and properties in the Vehicle class but also have some of their own additional functions and properties.
#
# Classes Car, Bike and Airplane all inherit the blueprint of class Vehicle, but in addition, they add their own blueprint. Now to create our new classes in a file called new_classes.py:

class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

# When we defined each of our classes, we typed Bike(Vehicle), Car(Vehicle), and Airplane(Vehicle). You could read each of these like "Make a class Bike/Car/Airplane that inherits from Vehicle". This is what is known as the implicit inheritance which allows us to use inherited attributes and methods of the Vehicle(parent) class in our new subclasses.

# MULTIPLE ARGUMENTS
# What if you want to pass in a variable number of arguments, or want to capture multiple arguments into a single parameter? Placing an asterisk before the name of the parameter after the "normal'' parameters does just that. The asterisk is called a 'splat' operator.

def varargs(arg1, *args):
  print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"

# In this example, the first argument is assigned to the first method parameter as usual. However, the next parameter is prefixed with an asterisk(the "splat" operator we just introduced), which bundles the remaining arguments into a new tuple, which is then assigned to that parameter.


# Super
# Sometimes in your OOP code, you will want to create updated versions of methods that are defined in the parent class, because in addition to your custom code you want specifically to call the parent implementation of that method as well (or instead). In these cases, you would reference that parent object with the keyword ' super'. Specifically you reference that parent's method by calling 'super(ChildClassName, self).parent_method()'.

# Parent __init__
# One thing we may want to do is call the Parent class's __init__ method, but also have our Child class change attributes defined by its Parent class. Say that we wanted each of our sub-classes (Wizard, Ninja, Samurai) to still inherit the attributes of the parent Human class but have more developed attributes than the average Human.  We could do that like this:

from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10           # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__()    # use super to call the Human __init__ method
        self.stealth = 10                # every Ninja starts off with 10 stealth
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__()  # use super to call the Human __init__ method
        self.strength = 10               # every Samurai starts off with 10 strength
    def sacrifice(self):
        self.health -= 5
