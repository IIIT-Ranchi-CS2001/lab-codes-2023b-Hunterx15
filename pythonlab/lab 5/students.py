#  Generate three lists using list comprehension. List of names, list of Roll nos
# and list of marks for Physics exam for all students of the class. Create a list
# of tuples using the zip function where each tuple carries individual student
# details. Sort the list of tuples using a sorted function by keeping Marks as the
# key for sorting.
names = list(map(str, input("Enter the names of the students: ").split()))
roll_nos = list(map(str, input("Enter the roll numbers of the students: ").split()))  
marks = list(map(int, input("Enter the marks of the students in Physics: ").split()))  
students = list(zip(names, roll_nos, marks))
sorted_students = sorted(students, key=lambda x: x[2],reverse=True)
for student in sorted_students:
    print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}")

