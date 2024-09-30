'''
Рецепт (Бакиев)
    Безе:
        - яйцо
        - сахар
'''

from recipe import Recipe

if __name__ == '__main__':
    receipt_from_api = {
        "title": "Безе",
        "ingredients_list": [
            ('Яйцо', 100, 50, 100),
            ('Сахар', 200, 100, 50),
        ],
    }

    recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    print(recipe)