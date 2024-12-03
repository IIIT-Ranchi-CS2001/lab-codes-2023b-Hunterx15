# . Write a python script to enter any string at run time and check
# whether it is a palindrome or not.
import string
x=str(input("Enter the string :"))
y=x[::-1]
if(x==y):
    print("string is palindrome !")
else:
    print("string is not a palindrome !")