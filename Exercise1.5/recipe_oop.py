#Step 1
class Recipe(object):
  
  all_ingredients = []
  
  #Initializaton method
  def __init__(self, name):
    self.name = name
    self.ingredients = []
    self.cooking_time = int() #or int(0)
    self.difficulty = ''

  #Method that updates the difficulty of the recipe
  def calculate_difficulty(self):
    if self.cooking_time < 10 and len(self.ingredients) < 4:
      difficulty = 'Easy' 
    elif self.cooking_time < 10 and len(self.ingredients) >= 4:
      difficulty = 'Medium'
    elif self.cooking_time >= 10 and len(self.ingredients) < 4:
      difficulty = 'Intermediate'
    elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
      difficulty = 'Hard'
    else:
      difficulty = 'Unknown'
    
    self.difficulty = difficulty
  
  #Step 2

  #Getter method for name
  def get_name(self):
    output = str(self.name) #or return self.name
    return output
  
  #Setter method for name
  def set_name(self):
    self.name = input('Enter the name of the recipe: ')

  #Getter method for cooking_time
  def get_cooking_time(self):
    output = int(self.cooking_time) #or return self.cooking_time
    return output

  #Setter method for cooking_time
  def set_cooking_time(self):
    self.cooking_time = int(input('Enter the cooking time (minutes) of the recipe: '))

  #Method that takes in variable-length arguments for the recipe’s ingredients and adds them to ingredients. Once all the ingredients are added, this function calls update_all_ingredients().
  def add_ingredients(self):
    recipe_ingredients = input('Enter the ingredients of the recipe (separated by commas): ')

    recipe_ingredients = recipe_ingredients.split(',')

    #Remove spaces and capitalize ingredients (strings)
    ingredient_list = [ingredient.strip().capitalize() for ingredient in recipe_ingredients]
    
    self.ingredients = ingredient_list

    self.update_all_ingredients()
  
  #Getter method for the ingredients that returns the list itself.
  def get_ingredients(self):
    output = self.ingredients
    return output
  
  #Getter method for difficulty which also calls calculate_difficulty() if difficulty hasn't been calculated.
  def get_difficulty(self):
    if self.difficulty == '':
      Recipe.calculate_difficulty(self)
    
    return self.difficulty
  
  #Search method that takes an ingredient as an argument, searches for it in the recipe, and returns True or False appropriately.
  def search_ingredient(self, ingredient):
    if ingredient.capitalize() in self.ingredients:
      return True
    else:
      return False
  
  #Method called that goes through the current object's ingredients and adds them to a class variable called all_ingredients, if they’re not already present. This class variable keeps track of all the ingredients that exist across all recipes.
  def update_all_ingredients(self):
    for ingredient in self.ingredients:
      if not ingredient in Recipe.all_ingredients:
        Recipe.all_ingredients.append(ingredient)
  
  #String representation that prints the entire recipe over a well formatted string.
  def __str__(self):
    output = '\nRecipe: ' + self.name + '\nCooking time (minutes): ' + str(self.cooking_time) + '\nIngredients: \n'
    for ingredient in self.ingredients:
      output += '-' + ingredient + '\n'
    output = output + 'Difficulty: ' + self.difficulty + '\n' + 30 * '-' 
    return output
  
#Step 3

#Method that find recipes that contain a specific ingredient
def recipe_search(data, search_term):
    for recipe in data:
      if recipe.search_ingredient(search_term):
        print(recipe)

#Step 4

recipes_list = []

print('Tea')
tea = Recipe('Tea')
tea.add_ingredients()
tea.set_cooking_time()
tea.get_difficulty()

recipes_list.append(tea)

#Step 5

print('Coffee')
coffee = Recipe('Coffee')
coffee.add_ingredients()
coffee.set_cooking_time()
coffee.get_difficulty()

recipes_list.append(coffee)

print('Cake')
cake = Recipe('Cake')
cake.add_ingredients()
cake.set_cooking_time()
cake.get_difficulty()

recipes_list.append(cake)

print('Banana Smoothie')
banana_smoothie = Recipe('Banana Smoothie')
banana_smoothie.add_ingredients()
banana_smoothie.set_cooking_time()
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)

print('Recipes List: ')
for recipe in recipes_list:
  print(recipe, end='\n')

print('\nSearch for recipes that contain each ingredient out of: Water, Sugar, Bananas.\n')

search_terms = ['Water', 'Sugar', 'Bananas']
for term in search_terms:
  print(30 * '-','Recipes that contain', term,30 * '-')
  if recipe_search(recipes_list, term):
    print(recipe)
  print('\n')


""" print('Testing the procedural attributes (methods) defined for the class (Step 2): ')

my_first_recipe = Recipe('Tea')

print('\nGet recipe name')
print(my_first_recipe.get_name())

print('\nSet cooking time')
my_first_recipe.set_cooking_time()

print('\nGet cooking time')
print(my_first_recipe.get_cooking_time())

print('\nAdd ingredients')
my_first_recipe.add_ingredients()

print('\nGet ingredients')
print(my_first_recipe.get_ingredients())

print('\nGet difficulty')
print(my_first_recipe.get_difficulty())

print('\nSearch for the ingredient "Tea Leaves"')
print(my_first_recipe.search_ingredient('Tea Leaves'))

print('\nGet all ingredients')
print(Recipe.all_ingredients)

print('\nString representation that prints the entire recipe over a well formated string')
print(my_first_recipe) """