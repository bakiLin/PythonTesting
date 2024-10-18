from recipe import Recipe
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        receipt_from_api = {
            "title": "Биг Макс",
            "ingredients_list": [
                ('Булки', 200, 200),
                ('Котлета', 150, 100),
                ('Овощи', 100, 80),
                ('Сыр', 30, 100),
                ('Соус', 5, 50)
            ],
        }

        recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])
        self.recipe_object = recipe

    def tearDown(self):
        del self.recipe_object

    def testOne(self):
        self.assertEqual(self.recipe_object.calc_price(), 530)

    def testTwo(self):
        self.assertEqual(self.recipe_object.calc_weight(), 485)

if __name__ == '__main__':
    unittest.main()