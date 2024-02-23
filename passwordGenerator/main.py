#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letters_g = symbols_g = numbers_g = ""
for letter in range(nr_letters):
  letters_g += random.choice(letters)
for symbol in range(nr_symbols):
  symbols_g += random.choice(symbols)
for number in range(nr_numbers):
  numbers_g += random.choice(numbers)
password_g = letters_g + symbols_g + numbers_g
print(f"Your password is: {password_g}")

# test line
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
pass_list = list(password_g)
print(pass_list)
random.shuffle(pass_list)
print(pass_list)
newpassword = ""
for alphanum in pass_list:
  newpassword += alphanum

print(newpassword)