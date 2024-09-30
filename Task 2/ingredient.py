class Ingredient:
    def __init__(self, name, weight, raw_weight, cost):
        self._name = name
        self._weight = weight
        self._raw_weight = raw_weight
        self._cost = cost

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
    def raw_weight(self):
        return self._raw_weight

    @raw_weight.setter
    def raw_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Raw weight is not int")
        self._weight = weight

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        if not isinstance(cost, (int, float)):
            raise TypeError("Cost is not int")
        self._cost = cost