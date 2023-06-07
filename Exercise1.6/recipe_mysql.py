#Part 1

#Sptep 1
import mysql.connector

#Step 2
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

#Step 3
cursor = conn.cursor()

#Step 4
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

#Step 5
cursor.execute("USE task_database")

#Step 6
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

#Part 2

def main_menu(conn, cursor):
  def calculate_difficulty(cooking_time, ingredient_list):
      if cooking_time < 10 and len(ingredient_list) < 4:
        difficulty = 'Easy' 
      elif cooking_time < 10 and len(ingredient_list) >= 4:
        difficulty = 'Medium'
      elif cooking_time >= 10 and len(ingredient_list) < 4:
        difficulty = 'Intermediate'
      elif cooking_time >= 10 and len(ingredient_list) >= 4:
        difficulty = 'Hard'
      else:
        difficulty = 'Unknown'
    
      return difficulty
   
  def create_recipe(conn, cursor):
    #Part 3
    name = input('Enter the name of the recipe: ')
    cooking_time = int(input('Enter the cooking time (minutes) of the recipe: '))
    ingredients = input('Enter the ingredients of the recipe (separated by commas): ')

    ingredients = ingredients.split(',')

    #Remove spaces and capitalize ingredients (strings)
    ingredient_list = [ingredient.strip().capitalize() for ingredient in ingredients]    

    ingredients_string = ', '.join(ingredient_list)

    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, ingredients_string, cooking_time, calculate_difficulty(cooking_time, ingredient_list))
    cursor.execute(sql, val)

    conn.commit()

  def search_recipe(conn, cursor):
    #Part 4
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall() #each row of the result is stored as an item in a list

    all_ingredients = []

    for row in results:
      recipe_ingredients = row[0].split(', ')
      for ingredient in recipe_ingredients:
        if not ingredient in all_ingredients:
          all_ingredients.append(ingredient)
    
    all_ingredients = list(enumerate(all_ingredients, 1))
    #print(all_ingredients)
    for position, value in all_ingredients:
      print('Ingredient ' + str(position) + ': ' + value)
    
    ingredient_number = int(input('Pick a number (ingredient) from the list: ')) 
    search_ingredient = all_ingredients[ingredient_number-1][1]

    sql = "SELECT name FROM Recipes WHERE ingredients LIKE %s"
    val = ['%' + search_ingredient + '%']
    cursor.execute(sql, val)

    results = cursor.fetchall()

    print('\nRecipes that contain', search_ingredient +':')
    for row in results:
      print(row[0])
    print()
 
  def update_recipe(conn, cursor):

    #Part 5
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    for row in results:
      print("ID: ", row[0])
      print("Name: ", row[1])
      print("Ingredients: ", row[2])
      print("Cooking time (minutes): ", row[3])
      print("Difficulty: ", row[4])
      print()

    recipe_id = int(input('Insert the ID of the recipe you want to update: '))
    print('What column of the recipe do you want update?')
    column_name = input('Type "name", "ingredients" or "time": ')
    new_value = input('Insert the new value: ')

    if column_name == 'ingredients':
      new_ingredient_list = new_value.split(',')
      cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", [recipe_id])
      results = cursor.fetchall()
      row = results[0] 
      cooking_time = row[0]
      difficulty = calculate_difficulty(cooking_time, new_ingredient_list)
      cursor.execute("UPDATE Recipes SET ingredients = %s, difficulty = %s WHERE id = %s", (new_value, difficulty, recipe_id))
    elif column_name == 'time':
      new_value = int(new_value)
      cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", [recipe_id])
      results = cursor.fetchall()
      row = results[0]
      #print(row[0])
      ingredient_list = row[0].split(',')
      difficulty = calculate_difficulty(new_value, ingredient_list)
      cursor.execute("UPDATE Recipes SET cooking_time = %s, difficulty = %s WHERE id = %s", (new_value, difficulty, recipe_id))
    elif column_name == 'name':
      cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (new_value, recipe_id))
    else:
      print('The column name is not valid.')

    conn.commit()

  def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    for row in results:
      print("ID: ", row[0])
      print("Name: ", row[1])
      print("Ingredients: ", row[2])
      print("Cooking time (minutes): ", row[3])
      print("Difficulty: ", row[4])
      print()
    
    recipe_id = int(input('Insert the ID of the recipe you want to delete: '))

    cursor.execute("DELETE FROM Recipes WHERE id = %s", [recipe_id])

    conn.commit()

  choice = ''
  while(choice != 'quit'):
    print('Pick a choice: ')
    print('1. Create a new recipe')
    print('2. Search for a recipe by ingredient')
    print('3. Update an existing recipe')
    print('4. Delete a recipe')
    print('Type "quit" to exit the program.')
    choice = input('Your choice: ')

    if choice == '1':
      create_recipe(conn, cursor)
    elif choice == '2':
      search_recipe(conn, cursor)
    elif choice == '3':
      update_recipe(conn, cursor)
    elif choice == '4':
      delete_recipe(conn, cursor)
    elif choice == 'quit':
      conn.commit()
      conn.close()
    else:
      print('Invalid choice.')

main_menu(conn, cursor)      
