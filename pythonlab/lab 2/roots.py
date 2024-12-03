# 5. Write a program to find the roots of a quadratic equation when the
# coefficients a, b and c are given ( assume that a, b and c are
# integers)
# Hint: find the discriminant d= b
# 2 − 4ac
# If d = 0, the equation has one real repeated root (both roots are the
# same:
# R1= R2 = -b/(2a)
# If d > 0, the equation has two distinct real roots.
# R1= (-b + sqrt(d))/2a
# R2= (-b - sqrt(d))/2a
# If d < 0, the equation has two complex roots.
# real_part = -b / (2 * a)
# imaginary_part = math.sqrt(-discriminant) / (2 * a)
import math
a= int(input("type the value of a :"))
b= int(input("type the value of b :"))
c= int(input("type the value of c :"))

d = math.sqrt(b*b - 4*a*c)
print(f"the discriminanat is :{d}")
r1 = (-b + d)/2*a
r2 = (-b - d)/2*a
if(d==0):
    print("the equation has one real repeated root!")
    print(f"root of the equation is : {r1}")
elif(d>0):
    print("the equation has two distinct real roots!")
    print(f"roots of the equation are : {r1} and {r2}")

else:
    print("the equation has two complex roots!")
    print(f"roots of the equation are : {r1} and {r2}")