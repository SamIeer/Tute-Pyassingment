#Task 1: Calculate Factorial Using a Function 
N = int(input("Enter a number : "))
def fact(n):
    if n <= 0: 
        return 0
    elif n==1 :
          return 1
    else : 
        return fact(n-1)*n
print(f"factorial of {N} is {fact(N)}")


#Task 2: Using the Math Module for Calculations
import math
N = int(input("Enter The Number :"))
print(f"Square root {math.sqrt(N)}")
print(f"logarithm {math.log(N)}")
print(f"sine {math.sin(N)}")
print(f"cosine {math.cos(N)}")