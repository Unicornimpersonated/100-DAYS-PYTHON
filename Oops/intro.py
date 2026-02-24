#student deatils
student_1=['Aneri',10] #Name and grade 
student_2=['Keshav',9]
student_3= 'Vishakha'

student_1.append('A')
print(student_1)

print(f'{student_1[0]} is in class {student_1[1]}')
print(f'{student_2[0]} is in class {student_2[1]}')
print('\n'+'*'*5)
# No proper structure , need to make from scratch every time
# We can use OOPs to create a class and then create objects of 
# that class to store the details of students in a proper  
# structure and we can also add functionfs to perform operations
# on those details.

# Using Oops - creating student records

#class - blueprint or template

class Student:
    name='Madhav'
    grade=10
    pass

student1= Student()
print(student1)
print(student1.name,student1.grade)

student2= Student()
print(student2)
print(student2.name,student2.grade)

# We can see that both the objects have the same details as we have
#  not changed the default values of the class attributes. We can change 
# the values of the attributes for each object

class Students:
    def __init__(self,full_name,class_grade):#method
        self.name = full_name
        self.grade = class_grade

    def student_details(self): #method
        return f'{self.name} is in class {self.grade}'

student_1= Students('Aneri',10)
print(student1.name,student1.grade)

student_2= Students('Keshav',9)
print(student_2.name,student_2.grade)


# method callf
student_1.student_details() #method call using object of the class
student_2.student_details()

# Self is a keyword which is used to refer to the current object of the class.
#  It is used to access the attributes and methods of the class. 
# It is used in the __init__ method to initialize the attributes of the class.

# Self is not a reserved keyword but it is a convention to use it as the 
# first parameter of the __init__ method. We can use any other name instead of self
#  but it is not recommended.

# self connects the attributes of the class to the object of the class. 
class Car:
    def __init__(self,model,year): # __init_ is a constructor which is used to initialize the attributes of the class.
        self.model=model #attribute of the class
        self.year=year

Kia=Car('Seltos',2020) # Object of the class Car
print(Kia.model)    