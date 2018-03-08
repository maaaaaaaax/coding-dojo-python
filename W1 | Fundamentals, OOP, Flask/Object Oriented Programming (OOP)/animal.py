class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayHealth(self):
        print self.health
        return self
class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)   # use super to call the Human __init__ method
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self
class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)   # use super to call the Human __init__ method
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print("I am a dragon")
        return self

prongs = Animal("Prongs", 100)
prongs.walk().walk().walk().run().run().displayHealth()
# output is 87

padfoot = Animal("Padfoot", 100)
prongs.walk().walk().walk().run().run().pet().displayHealth()
# output is 74

moony = Animal("Moony", 150)
moony.displayHealth()
# output is 150
