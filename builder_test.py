class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getConcession(self):
        concession = Concession()

        name = self.__builder.getName()
        concession.setName(name)

        weight = self.__builder.getWeight()
        concession.setWeight(weight)

        price = self.__builder.getPrice()
        concession.setPrice(price)

        return concession

# The whole product
class Concession:

    def __init__(self):
        self.__name     = None
        self.__weight   = None
        self.__price    = None

    def setName(self, name):
        self.__name = name

    def setWeight(self, weight):
        self.__weight = weight

    def setPrice(self, price):
        self.__price = price

    def specification(self):
        print("Name:", self.__name.name)
        print("Weight",  self.__weight.weight)
        print("Price",  self.__price.price)


class Builder:

    def getName(self): pass
    def getWeight(self): pass
    def getPrice(self): pass


class PopcornBuilder(Builder):

    def getName(self):
        name = Name()
        Name.name = "Popcorn"
        return name

    def getWeight(self):
        weight = Weight()
        weight.weight = "400g"
        return weight

    def getPrice(self):
        price = Price()
        price.price = "5e"
        return price

class NachoBuilder(Builder):

    def getName(self):
        name = Name()
        Name.name = "Nachos"
        return name

    def getWeight(self):
        weight = Weight()
        weight.weight = "500g"
        return weight

    def getPrice(self):
        price = Price()
        price.price = "6e"
        return price

class Name:
    name = None

class Weight:
    weight = None

class Price:
    price = None

def main():
    popcornBuilder = PopcornBuilder()
    nachoBuilder = NachoBuilder()

    director = Director()

    print("Popcorn")
    director.setBuilder(popcornBuilder)
    popcorn = director.getConcession()
    popcorn.specification()

    print("")

    print("Nacho")
    director.setBuilder(nachoBuilder)
    nacho = director.getConcession()
    nacho.specification()

if __name__ == "__main__":
    main()