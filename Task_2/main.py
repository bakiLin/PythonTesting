'''
Рецепт (Бакиев)
    Безе:
        - яйцо
        - сахар
        - соль
        - eggs
        - sugar
'''

from recipe import Recipe

if __name__ == '__main__':
    receipt_from_api = {
        "title": "Биг Мак",
        "ingredients_list": [
            ('Яйцо', 100, 50, 100),
            ('Сахар', 200, 100, 50),
            ('Соль', 100, 150, 70),
            ('Eggs', 120, 100, 100),
            ('Sugar', 300, 140, 90),
        ],
    }

    recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    print(recipe)