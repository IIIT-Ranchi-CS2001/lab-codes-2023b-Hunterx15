#  Generate three lists using list comprehension. List of names, list of Roll nos
# and list of marks for Physics exam for all students of the class. Create a list
# of tuples using the zip function where each tuple carries individual student
# details. Sort the list of tuples using a sorted function by keeping Marks as the
# key for sorting.
# 3. Redo question 2 without using zip and sorted functions.
names = list(map(str, input("Enter the names:").split()))  
roll_nos = list(map(str, input("Enter the roll numbers: ").split()))  
marks = list(map(int, input("Enter the marks: ").split()))
students = [(names[i], roll_nos[i], marks[i]) for i in range(len(names))]
for i in range(len(students)):
    for j in range(0, len(students) - i - 1):
        if students[j][2] > students[j + 1][2]:
            students[j], students[j + 1] = students[j + 1], students[j]

for student in students:
    print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}")
