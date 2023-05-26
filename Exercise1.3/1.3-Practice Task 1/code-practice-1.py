first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter the operator (+ or -): ")

if operator == '+':
  print("The sum of these numbers is", first_number + second_number)

elif operator == '-':
  print("The difference between these numbers is", first_number - second_number)

else:
  print("Unknown operator")