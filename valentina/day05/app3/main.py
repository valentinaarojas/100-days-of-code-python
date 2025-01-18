# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# use .choice() to choose random values from each list
# and .shuffle() to randomize order of characters in password

temp_list = [] # populate with random characters

for l in range(0, num_letters) :
    temp_list.append(random.choice(letters))

for s in range(0, num_symbols):
    temp_list.append(random.choice(symbols))

for n in range(0, num_numbers):
    temp_list.append(random.choice(numbers))

random.shuffle(temp_list) # shuffles order of characters in temp list

password = "".join(temp_list) # converts list into a string

print(f"\nYour password is: {password}\n")