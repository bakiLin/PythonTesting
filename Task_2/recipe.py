from ingredient import Ingredient

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

        self._set_ingredients()

    def _set_ingredients(self):
        self.ingredients = [Ingredient(element[0], element[1], element[2], element[3]) for element in self.ingredients]

    def calc_cost(self, portions=1):
        return sum([element.cost for element in self.ingredients]) * portions

    def calc_weight(self, portions=1, raw=True):
        return sum([element.raw_weight if raw else element.weight for element in self.ingredients]) * portions

    def __str__(self):
        return f'Рецепт {self.name} содержит:\n' + '\n'.join(
            [f'- {ingredient.name} - {ingredient.weight}г, {ingredient.cost}₽' for ingredient in self.ingredients])