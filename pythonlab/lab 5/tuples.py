# Generate two tuples to represent two distinct points in space. (Three
# dimensional geometry). Determine the Euclidian distance between the two
from math import sqrt
x=tuple(map(int,input("Enter the elements :").split()))
y=tuple(map(int,input("Enter the elements :").split()))
p=((x[0]-y[0])**2 + (x[1]-y[1])**2 + (x[2]-y[2])**2)
A=sqrt(p)
print(f"Euclidian distance between distinct : {A}")