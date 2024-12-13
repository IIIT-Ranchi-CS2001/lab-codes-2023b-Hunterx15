# Input a string from the user
# Enter a string. Determine the count of each letter present in the string using
# the concept of a dictionary
string = input("Enter a string: ")

letter_count = {}

for char in string:
    if char.isalpha():  
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1 
        else:
            letter_count[char] = 1  
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
