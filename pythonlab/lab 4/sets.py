# 4. Q4. Generate two sets - first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate following sets the

# a. of all artists of the class

# b. allrounders of the class
# difference(singers)
# c. dancers but not singers

# d. singers but not dancers

# e. dancers but not singers cum singers but not dancers
singers = set(map(str,input("Enter singer names :").split()))
# singers = {"Alice", "Bob", "Charlie", "David"}
dancers = set(map(str,input("Enter dancer names :").split()))
# dancers = {"Charlie", "Eve", "David", "Frank"}
all_artists = singers | dancers 
allrounders = singers & dancers
dancers_not_singers = dancers - singers

singers_not_dancers = singers - dancers 
dancers_singers_diff = dancers ^ singers  


print("a. All artists of the class:", all_artists)
print("b. Allrounders of the class:", allrounders)
print("c. Dancers but not singers:", dancers_not_singers)
print("d. Singers but not dancers:", singers_not_dancers)
print("e. Dancers but not singers combined with singers but not dancers:", dancers_singers_diff)
