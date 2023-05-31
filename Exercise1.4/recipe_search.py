#Step 1
import pickle

#Step 2
def display(recipe):
  print("Recipe: ", recipe['name'])
  print("Cooking time (min): ", recipe['cooking time'])
  print("Ingredients: ", *recipe['ingredients'], sep = "\n")
  print("Difficulty: ", recipe['difficulty'])
  print(sep = "\n")

""" test_recipe = {
  'name': 'Chá', 
  'cooking time': 5, 
  'ingredients': ['Água', 'Chá'], 
  'difficulty': 'Easy'  
  }
display(test_recipe)
exit() """

#Step 3
def search_ingredient(data):
  all_ingredients = list(enumerate(data['all ingredients'], 1))
  #print(all_ingredients)
  for position, value in all_ingredients:
    print("Ingredient " + str(position) + ": " + value)


  #Step 4
  try:
    ingredient_number = int(input("Pick a number (ingredient) from the list: ")) 
    ingredient_name = all_ingredients[ingredient_number-1][1]
  except:
    print("The input is incorrect.")
  else:
    for recipe in data['all recipes']:
      if ingredient_name in recipe['ingredients']:
        display(recipe)

#Step 5
try:
  recipe_data = input("What's the name of the file that contains your recipe data?")
  file = open(recipe_data, 'rb')
  data = pickle.load(file)
except FileNotFoundError:
  print("File not found.")
else:
  search_ingredient(data)


