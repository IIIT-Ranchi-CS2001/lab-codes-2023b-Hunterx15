# Write a python script using map, lambda and filter functions to do the following operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22 2@$” 
# To find all the letters given in the string and to convert them to uppercase
# o/p: [‘TOM’]
# To find all the digits present in the string and to find their squares
# o/p: [625]
# To display all the alphanumeric characters present in the string
# o/p: [“Tom”, ‘25’, “Rahu22”]


input_str = input("Enter a comma-separated string: ")
input_list = input_str.split()

# 1. Find all the letters in the string and convert them to uppercase
letters = list(filter(lambda x: x.isalpha(), input_list))
uppercase_letters = list(map(lambda x: x.upper(), letters))

# 2. Find all the digits in the string and compute their squares
digits = list(filter(lambda x: x.isdigit(), input_list))
squared_digits = list(map(lambda x: int(x)**2, digits))

# 3. Display all alphanumeric characters present in the string
alphanumeric = list(filter(lambda x: x.isalnum(), input_list))


print("Uppercase letters:", uppercase_letters)
print("Squared digits:", squared_digits)
print("Alphanumeric characters:", alphanumeric)
