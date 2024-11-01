from recipe import Recipe
import unittest

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")
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
        print("tearDown")
        del self.recipe_object

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_first(self):
        self.assertEqual(self.recipe_object.calc_cost(), 410)

    def test_second(self):
        self.assertEqual(self.recipe_object.calc_cost(2), 820)

    def test_third(self):
        self.assertEqual(self.recipe_object.calc_weight(2), 1080)

    def test_fourth(self):
        self.assertEqual(self.recipe_object.calc_weight(raw=True), 540)

if __name__ == '__main__':
    unittest.main()