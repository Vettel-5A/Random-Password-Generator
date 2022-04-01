import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
loop_count = nr_letters + nr_symbols + nr_numbers

number = 0
loop_count_letters = 0
loop_count_symbols = 0
loop_count_numbers = 0
new_password = []
password = str()
for number in range(0, loop_count):
  
  if loop_count_letters < nr_letters:
    new_letter = (letters[random.randint(0,51)])
    
  if loop_count_symbols < nr_symbols:
    new_symbol = (symbols[random.randint(0,8)])
    
  if loop_count_numbers < nr_numbers:
    new_number = (numbers[random.randint(0,9)])

  path_number = random.randint(0,2)
  if path_number == 0:
    if loop_count_letters < nr_letters:
        password += new_letter
      
  if path_number == 1:
    if loop_count_symbols < nr_symbols:
        password += new_symbol
      
  if path_number == 2:
    if loop_count_numbers < nr_numbers:
        password += new_number

print(f"Here is your password: {password}")