# 6. Create a program that manages employee salaries in a company using a
# dictionary. The dictionary should contain at least 5 employees, with their
# names as keys and their respective salaries as values [take user input data].
# Implement a sorting algorithm to arrange the employees in descending order
# based on their salaries without using any built-in sorting functions, and
# display the sorted list along with their salaries and rank (highest salary first
# and so on). [Hint: check the second parameter of the enumerate function].
# E.g.,
# 1. Cummins: Rs. 5000
# 2. Head: Rs. 4500
# 3. Maxwell: Rs. 2500
# 4. Narine: Rs. 1100
# 5. Rashid: Rs. 890

employees = {}

for i in range(5):
    name = input(f"Enter the name of employee {i+1}: ")
    salary = float(input(f"Enter the salary of {name}: Rs. "))
    employees[name] = salary

employee_items = list(employees.items())

for i in range(len(employee_items)):
    for j in range(0, len(employee_items) - i - 1):
        if employee_items[j][1] < employee_items[j + 1][1]:
            employee_items[j], employee_items[j + 1] = employee_items[j + 1], employee_items[j]

print("\nSorted Employee Salaries in Descending Order:")
for rank, (name, salary) in enumerate(employee_items, start=1):
    print(f"{rank}. {name}: Rs. {salary}")
    