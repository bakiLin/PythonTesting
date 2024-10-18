from recipe import Recipe

if __name__ == '__main__':
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

    print(recipe)