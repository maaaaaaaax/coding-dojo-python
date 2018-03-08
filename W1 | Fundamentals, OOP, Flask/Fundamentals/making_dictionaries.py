name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDictionary(lst1, lst2):
    temp = zip(lst1, lst2)
    dictionaryFromList = dict(temp)
    return dictionaryFromList

print makeDictionary(name, favorite_animal)
