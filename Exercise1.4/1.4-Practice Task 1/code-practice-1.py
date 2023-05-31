#Step 1
my_file = open('number_list.txt', 'w')

#Step 2
number_list = []
for i in range(50,101):
  number_list.append(i)

number_list = ["".join((str(number_list[i]),'\n')) for i in range(0,len(number_list))]
print(number_list)

#Step 3 and 4
with open('number_list.txt', 'w') as my_file:
  my_file.writelines(number_list)