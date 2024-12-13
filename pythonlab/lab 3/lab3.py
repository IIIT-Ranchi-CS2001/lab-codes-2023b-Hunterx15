# Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop
# Number    	Square
# 1              	1
# 2               	4
# …		            …
# n		            n

# n=int(input("Enter a number: "))
# i=1
# print("NUMBER      SQUARE")
# while(i<=n):
#     print("  ",i,"        ",i**2)
#     i=i+1

#                                                                           Program 10

#Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.

# n=int(input("Enter a number: "))
# i=n
# s=0
# while(i>0):
#     s=s+(i%10)
#     i=i//10
# print("Sum is:", s)


#                                                                           Program 11

# Write a python script to print the first n terms of the Fibonacci series using while loop
# n=int(input("Enter a number: "))
# a=0
# b=1
# print(a,b, end=" ")
# i=0
# c=0
# while(i<=n-2):
#     c=a+b
#     print(c, end=" ")
#     a=b
#     b=c
#     i=i+1


#                                                                           Program 12

#Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

# n=int(input("Enter number:"))
# m=int(input("Enter limit:"))
# i=1
# while(i<=m):
#     print(n, "* ",i," =" ,n*i)
#     i=i+1


#                                                                           Program 13

# Write a python script to check whether all the characters present in a string are alphanumeric 
# (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.

# s=str(input("Enter your string:"))
# b=True
# for i in s:
#     if((ord(i)<=57 and ord(i)>=48) or (ord(i)<=90 and ord(i)>=65) or (ord(i)<=122 and ord(i)>=97)):
#         continue
#     else:
#         b=False
#         break
# if(b==True):
#     print("TRUE")
# else:
#    print("FALSE")







#                                                                           Program 14

# Write a python script to find the number of occurrences of a particular character present in the given string using a loop.
#  (Don’t use string methods).

s=str(input("Enter string:"))
a=str(input("Enter character:"))
count=0
for i in s:
    if(i==a):
        count=count+1
print("Number of occurence is:",count)