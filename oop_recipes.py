# словарь, составленный на основе файла recipes.txt

cook_book = {}
recipe_name = ''

with open('recipes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.isnumeric():
        continue
    if not recipe_name:
        recipe_name = line
        cook_book[recipe_name] = []
    elif ' | ' in line:
        ingredients = line.split(' | ')
        ingredient_name = ingredients[0]
        quantity = int(ingredients[1])
        measure = ingredients[2].strip()
        cook_book[recipe_name].append({'ingredient_name': ingredient_name,
                                       'quantity': quantity, 'measure': measure})
    else:
        recipe_name = line
        cook_book[recipe_name] = []

print("cook_book = {")
for recipe, ingredients in cook_book.items():
    print(f"  '{recipe}': [")
    for ingredient in ingredients:
        print(f"    {{'ingredient_name': '{ingredient['ingredient_name']}', 'quantity': {ingredient['quantity']}, "
              f"'measure': '{ingredient['measure']}'}}")
    print("  ],")
print("}")


