#RECURSIVE FUNCTION
#Problem:create a recursive function to calculate the factoial of a number
#Recursion means a function calling itself to solve a problem step by step.(recursion->repetition)
# in recursion like problem think of exit strategy

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))