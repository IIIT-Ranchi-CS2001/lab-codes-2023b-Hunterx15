#  Enter the following details of a student at run time: - Name, Roll
# number and marks secured for Mathematics Examination out of 100.
# Write a python script to display student details as shown:
# Name:
# Roll Number:
# Marks:
# Grade Point:
# Remark:
# The criteria for awarding grade point and remark are as given in the
# table:
Name = input("Enter your name :")
Roll_number=input("Enter your roll number :")
Marks = int(input("Enter your marks :"))
Grade= 0
if(Marks>=90):
   Grade = 10
   print(f"Grade: {Grade}")
   print("Remark: OUTSTANDING!")
elif(Marks<90 and Marks>=80):
   Grade =9
   print(f"Grade: {Grade}")
   print("Remark: VERY GOOD")
elif(Marks<80 and Marks>=70):
   Grade =8
   print(f"Grade: {Grade}")
   print("Remark: GOOD")
elif(Marks<70 and Marks>=60):
   Grade =7
   print(f"Grade: {Grade}")
   print("Remark: AVERAGE")
elif(Marks<60 and Marks>=50):
   Grade =6
   print(f"Grade: {Grade}")
   print("Remark: PASS")
else:
   Grade =0
   print(f"Grade: {Grade}")
   print("Remark: FAIL")