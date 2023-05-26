recipes_list = []
ingredient_list = []

def take_recipe ():
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time (min) of the recipe: "))
  ingredients = input("Enter the ingredients of the recipe (separated by commas): ")

  ingredient_list = ingredients.split(',')
  #remove spaces and capitalize ingredients (strings)
  ingredient_list = [ingredient.strip().capitalize() for ingredient in ingredient_list]


  recipe = {
    'name': name,
    'cooking time': cooking_time,
    'ingredients': ingredient_list
  }

  return recipe

n = int(input("How many recipes would you like to enter? "))

for r in range(0, n):
  recipe = take_recipe()

  for ingredient in recipe['ingredients']:
    if not(ingredient in ingredient_list):
      ingredient_list.append(ingredient)

  recipes_list.append(recipe)

for recipe in recipes_list:
  if recipe['cooking time'] < 10 and len(recipe['ingredients']) <= 4:
    difficulty = 'Easy' 
  elif recipe['cooking time'] >= 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Intermediate'
  elif recipe['cooking time'] >= 10 and len(recipe['ingredients']) >= 4:
    difficulty = 'Hard'
  else:
    difficulty = 'Unknown'

  print("Recipe: ", recipe['name'])
  print("Cooking time (min): ", recipe['cooking time'])
  print("Ingredients: ", *recipe['ingredients'], sep = "\n")
  print("Difficulty: ", difficulty)
  print(sep = "/n")

ingredient_list.sort(key=str.lower)
print("Ingredients Available Across All Recipes")
print("----------------------------------------")
print(*ingredient_list, sep = "\n")



  

