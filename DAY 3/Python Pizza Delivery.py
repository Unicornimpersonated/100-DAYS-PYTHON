print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
jalapeno = input("Do you want jalapeno on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese ?Y or N: ")

#todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25

else:
    print("You typed wrong inputs.")

if jalapeno == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill +=1

print(f"Total bill is {bill}")