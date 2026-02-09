numbet_to_check = int(input("Enter the number you want to check "))
print(numbet_to_check % 2) #modulo
print(numbet_to_check // 2) #ans in int
print(numbet_to_check / 2) #ans in float

if numbet_to_check % 2 == 0:
    print("It is even number")
else:
    print("It is odd number")