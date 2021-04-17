class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getConcession(self):
        concession = Concession()

        name = self.__builder.getName()
        concession.setName(name)

        quantity = self.__builder.getQuantity()
        concession.setQuantity(quantity)

        price = self.__builder.getPrice()
        concession.setPrice(price)

        return concession

# The whole product
class Concession:

    def __init__(self):
        self.__name     = None
        self.__quantity   = None
        self.__price    = None

    def setName(self, name):
        self.__name = name

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def setPrice(self, price):
        self.__price = price

    def getName(self):
        return self.__name.name

    def getQuantity(self):
        return self.__quantity.quantity

    def getPrice(self):
        return self.__price.price

    def specification(self):
        return f"Name: {self.__name.name}, Quantity: {self.__quantity.quantity}, Price: {self.__price.price}"


class Builder:

    def getName(self): pass
    def getQuantity(self): pass
    def getPrice(self): pass


class PopcornBuilder(Builder):

    def getName(self):
        name = Name()
        name.name = "Popcorn"
        return name

    def getQuantity(self):
        quantity = Quantity()
        quantity.quantity = "400g"
        return quantity

    def getPrice(self):
        price = Price()
        price.price = 5
        return price

class NachoBuilder(Builder):

    def getName(self):
        name = Name()
        name.name = "Nachos"
        return name

    def getQuantity(self):
        quantity = Quantity()
        quantity.quantity = "500g"
        return quantity

    def getPrice(self):
        price = Price()
        price.price = 6
        return price

class ColaBuilder(Builder):

    def getName(self):
        name = Name()
        name.name = "Cola"
        return name

    def getQuantity(self):
        quantity = Quantity()
        quantity.quantity = "1L"
        return quantity

    def getPrice(self):
        price = Price()
        price.price = 4
        return price

class HotDogBuilder(Builder):

    def getName(self):
        name = Name()
        name.name = "Hot Dog"
        return name

    def getQuantity(self):
        quantity = Quantity()
        quantity.quantity = "350g"
        return quantity

    def getPrice(self):
        price = Price()
        price.price = 5
        return price

class Name:
    name = None

class Quantity:
    Quantity = None

class Price:
    price = None
