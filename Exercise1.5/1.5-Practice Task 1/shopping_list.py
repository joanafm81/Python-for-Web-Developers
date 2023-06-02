#Step 2
class ShoppingList(object):
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  def add_item(self, item):
      if not(item in self.shopping_list):
        self.shopping_list.append(item)
    
  def remove_item(self, item):
      self.shopping_list.remove(item)

  def view_list(self):
      print(self.shopping_list)

#Step 3
pet_store_shopping_list = ShoppingList('Pet Store Shopping List')

print('Step 3')
print(pet_store_shopping_list.list_name)

#Step 4
pet_store_shopping_list.add_item('dog food')
pet_store_shopping_list.add_item('frisbee')
pet_store_shopping_list.add_item('bowl')
pet_store_shopping_list.add_item('collars')
pet_store_shopping_list.add_item('flea collars')

print('Step 4')
pet_store_shopping_list.view_list()

#Step 5
print('Step 5')
pet_store_shopping_list.remove_item('flea collars')

pet_store_shopping_list.view_list()

#Step 6
print('Step 6')
pet_store_shopping_list.add_item('frisbee')

pet_store_shopping_list.view_list()

#Step 7
print('Step 7')
pet_store_shopping_list.view_list()