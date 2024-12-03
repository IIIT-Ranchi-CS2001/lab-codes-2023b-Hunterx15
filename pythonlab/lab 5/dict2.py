#  Create a dictionary containing user-inputted names and marks (in
# percentage) for 5 students. Write a Python program that classifies these
# students into three categories: "High Performers" (marks ≥ 85), "Average
# Performers" (60 ≤ marks < 85), and "Low Performers" (marks < 60). The
# program should print the number of students in each category along with
# their names. Finally, identify and display the name of the student with the
# highest marks.


students = {}

for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks (in %) for {name}: "))
    students[name] = marks


high_performers = []
average_performers = []
low_performers = []


for name, marks in students.items():
    if marks >= 85:
        high_performers.append(name)
    elif 60 <= marks < 85:
        average_performers.append(name)
    else:
        low_performers.append(name)

print("\nHigh Performers (marks ≥ 85):")
print(f"Count: {len(high_performers)}, Names: {', '.join(high_performers) if high_performers else 'None'}")

print("\nAverage Performers (60 ≤ marks < 85):")
print(f"Count: {len(average_performers)}, Names: {', '.join(average_performers) if average_performers else 'None'}")

print("\nLow Performers (marks < 60):")
print(f"Count: {len(low_performers)}, Names: {', '.join(low_performers) if low_performers else 'None'}")

# Identify and display the student with the highest marks
highest_scorer = max(students, key=students.get)
print(f"\nThe student with the highest marks is: {highest_scorer} with {students[highest_scorer]}%")
