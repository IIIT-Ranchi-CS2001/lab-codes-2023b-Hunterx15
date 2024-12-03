# Find the sum of n terms of exponential series -
# cosx = 1 - x2/2! + x4/4!........
# use recursion 

import math
def cos_series_recursive(x, n):
    if n == 0:
        return 1
    else:
        term = ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
        return term + cos_series_recursive(x, n-1)
x = float(input("Enter the value of x in cos(x):"))
n = int(input("Enter the n term to find the sum of series :"))
result = cos_series_recursive(x, n)
print(f"The sum of the first {n} terms of the cos(x) series is: {result}")

