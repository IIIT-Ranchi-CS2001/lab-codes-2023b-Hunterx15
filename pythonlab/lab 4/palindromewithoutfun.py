# find the number of palindrome words without using any function 


input_string = str(input("Enter your string :"))
words = input_string.split()
count = 0
for word in words:
     if(word == word[::-1]):
      count += 1

print("Number of palindrome words:", count)

