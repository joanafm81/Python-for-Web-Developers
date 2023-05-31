#Step 1
import pickle

#Step 2
recipe = {
  'name': 'Tea',
  'ingredients': ['Tea leaves', 'Water', 'Sugar'],
  'cooking time': 5,
  'difficulty': 'Easy'
}
print(recipe)

#Step 3
my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()

#Step 4
with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details - ")
print("Name:  ", recipe['name'])
print("Ingredients:  ", *recipe['ingredients'], sep = "\n")
print("Cooking time: ", recipe['cooking time'], "minutes")
print("Difficulty: ", recipe['difficulty'])