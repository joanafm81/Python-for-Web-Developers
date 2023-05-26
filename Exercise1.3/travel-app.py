destination = input('Where do you want to travel? ')
destination = destination.strip().capitalize()
if destination == 'Berlin' or destination == 'London' or destination == 'Paris':
  print('Enjoy your stay in ' + destination + '!')
else:
  print('Oops, that destination is not currently available.')
