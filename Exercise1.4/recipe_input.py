#Step 1
import pickle

recipes_list = []
all_ingredients = []

#Step 2

def take_recipe():
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time (min) of the recipe: "))
  ingredients = input("Enter the ingredients of the recipe (separated by commas): ")

  ingredient_list = ingredients.split(',')
  #Remove spaces and capitalize ingredients (strings)
  ingredient_list = [ingredient.strip().capitalize() for ingredient in ingredient_list]

  recipe = {
    'name': name,
    'cooking time': cooking_time,
    'ingredients': ingredient_list
  }

  recipe['difficulty'] = calc_difficulty(recipe)

  return recipe

#Step 3

def calc_difficulty(recipe):
  if recipe['cooking time'] < 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Easy' 
  elif recipe['cooking time'] < 10 and len(recipe['ingredients']) >= 4:
    difficulty = 'Medium'
  elif recipe['cooking time'] >= 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Intermediate'
  elif recipe['cooking time'] >= 10 and len(recipe['ingredients']) >= 4:
    difficulty = 'Hard'
  else:
    difficulty = 'Unknown'

  return difficulty

""" test_recipe = take_recipe()
print(test_recipe)
exit() """

#Step 4
try:
  filename = input("Enter a filename to store your recipes: ")
  file = open(filename, 'rb')
  data = pickle.load(file)
except FileNotFoundError:
  print("File not found. A new file will be created.")
  data = {
    'all recipes': [], 
    'all ingredients': [] 
    }
except:
  print("An unexpected error occurred.")
  data = {
    'all recipes': [], 
    'all ingredients': [] 
    }
else:
  file.close()
finally:
  recipes_list = data['all recipes']
  all_ingredients = data['all ingredients']

print(recipes_list)
print(all_ingredients)

#Step 5
n = int(input("How many recipes would you like to enter? "))

for r in range(0, n):
  recipe = take_recipe()

  for ingredient in recipe['ingredients']:
    if not(ingredient in all_ingredients):
      all_ingredients.append(ingredient)

  recipes_list.append(recipe)

data = {
   'all recipes': recipes_list,
   'all ingredients': all_ingredients
  }

new_file = open(filename, 'wb')
pickle.dump(data, new_file)
new_file.close()