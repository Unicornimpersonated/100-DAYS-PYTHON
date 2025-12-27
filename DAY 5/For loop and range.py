fruits = ["Apple", "Peach", "Strawberry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie ")
    print(fruits)

print(fruits)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_exam_score = sum(student_scores)
print(total_exam_score)
max_exam_score = max(student_scores)

sum = 0

for score in student_scores:
    sum += score
    print(f" Total score of the students are {sum}" )
    #max_exam_score = max(total_score)
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f" The maximum score is {max_score}")



print(range(1,10))
for number in range(1,11):
    print(number)
print("\n")
print("increasing the steps")
for number in range(0,100,3):
    print(number)

total = 0
for number in range(1,101):
    total+=number
print(total)