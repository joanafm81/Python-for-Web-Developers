#Part 1
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

#Step 4 - Create an engine object called engine that connects to your desired database
engine = create_engine("mysql://cf-python:password@localhost/task_database")

#Step 5 - Make the session object that you’ll use to make changes to your database
Session = sessionmaker(bind=engine)
session = Session()

#Part 2
Base = declarative_base()

#Steps 1, 2, 3, 4 and 5
class Recipe(Base):
  __tablename__ = "final_recipes"

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(50))
  ingredients = Column(String(255))
  cooking_time = Column(Integer)
  difficulty = Column(String(20))

  def __repr__(self):
    return "Recipe ID-Name: " + str(self.id) + "-" + self.name
  
  def __str__(self):
    output = "\nRecipe: " + self.name + "\nCooking time (minutes): " + str(self.cooking_time) + "\nIngredients: \n"
    ingredient_list = self.ingredients.split(', ')
    for ingredient in ingredient_list:
      output += "-" + ingredient + "\n"
    output = output + "Difficulty: " + self.difficulty + "\n" + 30 * "-" 
    return output
  
  #Step 5
  def calculate_difficulty(self):
    ingredient_list = self.return_ingredients_as_list()

    if self.cooking_time < 10 and len(ingredient_list) < 4:
      difficulty = 'Easy' 
    elif self.cooking_time < 10 and len(ingredient_list) >= 4:
      difficulty = 'Medium'
    elif self.cooking_time >= 10 and len(ingredient_list) < 4:
      difficulty = 'Intermediate'
    elif self.cooking_time >= 10 and len(ingredient_list) >= 4:
      difficulty = 'Hard'
    else:
      difficulty = 'Unknown'
  
    self.difficulty = difficulty
  
  #Step 6
  def return_ingredients_as_list(self):
    if self.ingredients == '':
      ingredient_list = []
      return ingredient_list
    else:
      ingredient_list = self.ingredients.split(', ')
      return ingredient_list

#Step 8 - Create the corresponding table on the database using the create_all() method from Base.metadata

Base.metadata.create_all(engine) 

#Part 3

#Function 1: create_recipe()

def create_recipe():

  pendingInput = True
  name = ''
  while pendingInput:
    name = input("Enter the name of the recipe: ")

    if len(name) <= 50 and name.replace(' ','').isalnum():
      pendingInput = False
    else:
      print("The name of the recipe must not extend past 50 characters and must contain only alphanumeric characters. ")

  name = name.capitalize()

  pendingInput = True
  while pendingInput:
    cooking_time = int(input("Enter the cooking time (minutes) of the recipe: "))

    if cooking_time > 0:
      pendingInput = False
    else:
      print("The cooking time must be a positive number. ")

  ingredients = []
  pendingInput = True
  number_of_ingredients = 0
  while pendingInput:
    number_of_ingredients = int(input("How many ingredients would you like to enter? "))

    if number_of_ingredients > 0:
      pendingInput = False
    else:
      print("Enter a valid, positive number.")

  chars_left = 255 - 2 * (number_of_ingredients - 1) #chars_left takes in consideration the comma plus space between each ingredient
  for i in range(1,number_of_ingredients+1):

    pendingInput = True
    while pendingInput:

      ingredient = input("Enter ingredient number " + str(i) + " (" + str(chars_left) + " letters left): ")
      ingredient_length = len(ingredient)

      if ingredient.replace(' ','').isalpha() and chars_left > ingredient_length:
        pendingInput = False
        ingredients.append(ingredient)
        chars_left = chars_left-ingredient_length
      elif not ingredient.isalpha() and ingredient.isspace():
        print("Enter a valid ingredient with letters only.")
      else:
        print("Ingredient must have", chars_left,"letters or less.")

  #Remove spaces and capitalize ingredients (strings)
  ingredients = [ingredient.strip().capitalize() for ingredient in ingredients]

  string_of_ingredients = ', '.join(ingredients)
  
  recipe_entry = Recipe(
        name = name,
        cooking_time = cooking_time,
        ingredients = string_of_ingredients,
        )
  recipe_entry.calculate_difficulty()
  
  session.add(recipe_entry)

  session.commit()

#Function 2: view_all_recipes()

def view_all_recipes():
  number_of_entries = session.query(Recipe).count()

  if number_of_entries == 0:
    print("There aren't any recipes in the database.")
    return None
  else:
    all_recipes_list = session.query(Recipe).all()
    for recipe in all_recipes_list:
      print(recipe)

#Function 3: search_by_ingredients()

def search_by_ingredients():
  number_of_entries = session.query(Recipe).count()

  if number_of_entries == 0:
    print("There aren't any recipes in the database.")
    return None
  
  results = session.query(Recipe).all()
  
  all_ingredients = []

  for result in results:
    temporary_list = result.ingredients.split(', ')
    for ingredient in temporary_list:
      if not ingredient.capitalize() in all_ingredients:
        all_ingredients.append(ingredient.capitalize())

  all_ingredients = list(enumerate(all_ingredients, 1))
  for position, value in all_ingredients:
      print('Ingredient ' + str(position) + ': ' + value)
    
  ingredient_numbers = input("Pick the ingredients that you would like to search for recipes (type the numbers separated by spaces): ")

  ingredient_numbers_list = ingredient_numbers.split(' ')

  search_ingredients = []

  for ingredient_number in ingredient_numbers_list:
    ingredient_number = int(ingredient_number)
    if ingredient_number < 0 or ingredient_number > len(all_ingredients):
      print("Option", ingredient_number,"is not available.")
      return None
    else:
      ingredient_string = all_ingredients[ingredient_number-1][1]
      search_ingredients.append(ingredient_string)
  
  conditions = []

  for ingredient in search_ingredients:
    like_term = "%" + ingredient + "%"
    conditions.append(Recipe.ingredients.like(like_term))
  
  recipes_search_list = session.query(Recipe).filter(*conditions).all()

  for recipe in recipes_search_list:
    print(recipe)

#Function 4: edit_recipe()

def edit_recipe():
  number_of_entries = session.query(Recipe).count()

  if number_of_entries == 0:
    print("There aren't any recipes in the database.")
    return None
  
  results = session.query(Recipe).all()

  for result in results:
    print("Recipe ID", result.id, "-", result.name)

  chosen_recipe = int(input("Pick a recipe (type the ID): "))

  if chosen_recipe < 1:
    print("The chosen ID doesn't exist.")
    return None
  
  recipe_to_edit = session.query(Recipe).get(chosen_recipe)
  if recipe_to_edit == None:
    print("There is no recipe ID", chosen_recipe + ".")
    return None

  print("Chosen recipe: ", recipe_to_edit.id)
  print("1. Name: ", recipe_to_edit.name)
  print("2. Ingredients: ", recipe_to_edit.ingredients)
  print("3. Cooking time (minutes): ", recipe_to_edit.cooking_time)
  attribute_to_edit = int(input("Pick the attribute you would like to edit (enter the corresponding number): "))

  if attribute_to_edit < 1 or attribute_to_edit > 3:
    print("The chosen attribute doesn't exist. Please pick a number between 1 and 3.")
    return None

  if attribute_to_edit == 1:
    pendingInput = True
    name = ''
    while pendingInput:
      name = input("Enter the name of the recipe: ")
      if len(name) <= 50 and name.replace(' ','').isalnum():
        pendingInput = False
      else:
        print("The name of the recipe must not extend past 50 characters and must contain only alphanumeric characters. ")
    
    session.query(Recipe).filter(Recipe.id == chosen_recipe).update({Recipe.name: name})
    print("Recipe name updated.")

  elif attribute_to_edit == 2:
    ingredients = []
    pendingInput = True
    number_of_ingredients = 0
    while pendingInput:
      number_of_ingredients = int(input("How many ingredients would you like to enter? "))

      if number_of_ingredients > 0:
        pendingInput = False
      else:
       print("Enter a valid, positive number.")

    chars_left = 255 - 2 * (number_of_ingredients - 1) #chars_left takes in consideration the comma plus space between each ingredient
    for i in range(1,number_of_ingredients+1):

      pendingInput = True
      while pendingInput:

        ingredient = input("Enter ingredient number " + str(i) + " (" + str(chars_left) + " letters left): ")
        ingredient_length = len(ingredient)

        if ingredient.replace(' ','').isalpha() and chars_left > ingredient_length:
          pendingInput = False
          ingredients.append(ingredient)
          chars_left = chars_left-ingredient_length
        elif not ingredient.isalpha():
          print("Enter a valid ingredient with letters only.")
        else:
          print("Ingredient must have", chars_left,"letters or less.")

    string_of_ingredients = ', '.join(ingredients)

    recipe_to_edit.calculate_difficulty()
    print(recipe_to_edit.difficulty)
    session.query(Recipe).filter(Recipe.id == chosen_recipe).update({Recipe.ingredients: string_of_ingredients, Recipe.difficulty: recipe_to_edit.difficulty})
    print("Recipe ingredients updated.")


  elif attribute_to_edit == 3:
    pendingInput = True
    while pendingInput:
      cooking_time = int(input("Enter the cooking time (minutes) of the recipe: "))

      if cooking_time > 0:
        pendingInput = False
      else:
        print("The cooking time must be a positive number. ")

    recipe_to_edit.calculate_difficulty()
    print(recipe_to_edit.difficulty)
    session.query(Recipe).filter(Recipe.id == chosen_recipe).update({Recipe.cooking_time: cooking_time, Recipe.difficulty: recipe_to_edit.difficulty})
    print("Recipe cooking time updated.")
    
  session.commit()

#Estou a repetir as validações da primeira função. Como posso melhorar a legibiidade e eficiência?

#Function 5: delete_recipe()

def delete_recipe():
  number_of_entries = session.query(Recipe).count()

  if number_of_entries == 0:
    print("There aren't any recipes in the database.")
    return None
  
  results = session.query(Recipe).all()

  print(results)

  chosen_recipe = int(input("Pick a recipe (type the ID): "))

  if chosen_recipe < 1:
    print("The chosen ID doesn't exist.")
    return None
  
  recipe_to_delete = session.query(Recipe).get(chosen_recipe)
  if recipe_to_delete == None:
    print("There is no recipe ID", chosen_recipe + ".")
    return None

  confirmation = input("Are you sure you want to delete this recipe? Type 'Yes' to confirm or 'No' to cancel. ")

  if confirmation == 'Yes':
    session.delete(recipe_to_delete)
    print("Recipe deleted.")
  elif confirmation == 'No':
    print("Operation canceled.")
    return None
  else:
    print("That's not a valid answer. Please type 'Yes' to confirm (delete recipe) or 'No' to cancel.")
    return None
  
  session.commit()

choice = ''
while(choice != 'quit'):
  print("Main Menu" + "\n" + 30 * "=" )
  print("Pick a choice: ")
  print("1. Create a new recipe")
  print("2. View all recipes")
  print("3. Search for a recipe by ingredient")
  print("4. Update an existing recipe")
  print("5. Delete a recipe")
  print("'quit': Quit the application")
  choice = input("Your choice: ")

  if choice == '1':
    create_recipe()
  elif choice == '2':
    view_all_recipes()
  elif choice == '3':
    search_by_ingredients()
  elif choice == '4':
    edit_recipe()
  elif choice == '5':
    delete_recipe()
  elif choice == 'quit':
    session.close()
    #engine close()????
  else:
    print('Invalid choice.')
      