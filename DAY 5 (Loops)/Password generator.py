import random

letters =['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!' ,'#' ,'$', '%', '(', ')', '*', '+']

print("Welcome to the PyPassword generator!!")
nr_letters = int(input("How many letters do you like in your password\n"))
nr_symbols = int(input("How many symbols do you like \n"))
nr_numbers = int(input("How many numbers do you like \n"))

# easy level
password =""

for char in range(0, nr_letters  ):
    password+= random.choice(letters)

for char in range(0, nr_symbols  ):
    password+= random.choice(symbols)

for char in range(0, nr_numbers  ):
    password+= random.choice(numbers)

print(password)

print("\n")
print("\n")

nr_letters = int(input("How many letters do you like in your password\n"))
nr_symbols = int(input("How many symbols do you like \n"))
nr_numbers = int(input("How many numbers do you like \n"))
# Hard level
password_list = []

for char in range(0, nr_letters ):
    password_list.append( random.choice(letters))

for char in range(0, nr_symbols  ):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers  ):
    password_list.append( random.choice(numbers))

print(password_list)
# shuffle
random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password +=char

print(f"Your password is:{password}")