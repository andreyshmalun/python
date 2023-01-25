import pickle

# Calculating the difficulty of the recipe


def calc_difficulty(recipe):
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficluty'] = 'Easy'

    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficluty'] = 'Medium'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficluty'] = 'Intermediate'

    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficluty'] = 'Hard'

# A function to take recipes from the user


def take_recipe():
    name = str(input("Enter the name of your recipe: "))
    cooking_time = int(
        input("Enter the cooking time for your recipe in minutes: "))
    ingredients = input("Enter the ingredients for your recipe: ")
    ingredients = ingredients.split()
    ingredients = [ingredient.lower() for ingredient in ingredients]
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients
              }
    difficluty = calc_difficulty(recipe)
    return recipe


# Get file with recipes from user
recipes_list = []
all_ingredients = []

filename = str(input("Enter a filename with your recipes: "))
try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print("File not found. Creating a new file.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("Unexpected error. Creating a new file. ")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

# Enter recipes details from user
num = int(input('How many recipes would you like to enter? '))

for i in range(num):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = str(input('Enter a name for new file. '))
new_file_name = open(new_file_name, 'wb')
pickle.dump(data, new_file_name)
