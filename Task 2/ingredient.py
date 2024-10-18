#(Б)акиев -> (Б)иг Мак

class Ingredient:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is not string")
        self._name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight is not int")
        self._weight = weight

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Cost is not int")
        self._price = price