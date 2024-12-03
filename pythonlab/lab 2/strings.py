#  For the given string S=”Ba Ba Black Sheep”, determine the following
# using built in functions:
# a. The length of the string S
# b. The first occurrence of the letter ‘e’
# c. The total number of occurrences of ‘a’
# d. Generate “Ta Ta Black Sheep”
import string
s="Ba Ba Black Sheep"
print("length of the string is :",len(s))
print("first occurence of the letter 'e' is ", s.index("e"))
print("The total number of occurrences of 'a'",s.count('a'))
s= s.replace("B","T",2)
print(s)