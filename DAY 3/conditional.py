# If else statement
water_level= float(input("What is the level of water?"))
if water_level>50:
      print("Drain water!")
else:
      print("Continue!")


print("Welcome to the Rollercoaster!!")
height= int(input("Enter the height in cm "))
if height>120:
      print("You can ride the Rollercoaster!")
else:
      print("Sorry you have to grow tall to ride the Rollercoaster!")

#Nested if else statement



print("Welcome to the ride!!")
height=int(input("Enter height in cm "))
age=int(input("Enter the age in years "))

# execute one condition
if height>120:
      if age<=12:
            print("Pay $5")

      elif age<18:
            print("Pay $7")
      else:
            print("Pay $14")
else:
      print("You cannot ride")

# execute multiple conditions
print("Welcome to the ride!!")
height=int(input("Enter height in cm "))
age=int(input("Enter the age in years "))

bill = 0
if height>120:
      if age<=12:
            print("Child tickets are $5")
            bill = 5

      elif age<18:
            print("youth tickets are $7")
            bill = 7

      else:
            print("Adult tickets are $14")
            bill = 14

      wants_photo = input("Do you want to have a photo take? Type y for Yes or n for No. ")
      if wants_photo == "y":
            #Adds $3 to their bill
            bill = bill + 3

      print(f" The total bill is ${bill}")
else:
      print("You cannot ride")
